from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django_filters.views import FilterView

from .filter import FlatFilter
from .forms import FlatForm, ImageInlineFormSet, LocationInlineFormSet, UpdateFlatForm, DetailInlineFormSet, \
    ImageUpdateForm, DetailUpdateForm, UpdateLocationForm, UpdateImageInlineFormSet
from .models import Flat, Equip, FlatDetail, FlatLocation, FlatImage
from message.forms import MessageForm
from message.models import Message, Chat

User = get_user_model()


class HomeListView(ListView):
    model = Flat
    template_name = 'home.html'
    context_object_name = 'flats'
    ordering = ['-created_at']


class FlatCreateView(LoginRequiredMixin, CreateView):
    template_name = 'create.html'
    model = Flat
    form_class = FlatForm
    login_url = 'login'
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super(FlatCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['detail_items'] = DetailInlineFormSet(self.request.POST, prefix='detail_item_set')
            context['location_items'] = LocationInlineFormSet(self.request.POST, prefix='location_item_set')
            context['image_items'] = ImageInlineFormSet(self.request.POST, prefix='image_item_set')
        else:
            context['detail_items'] = DetailInlineFormSet(prefix='detail_item_set')
            context['location_items'] = LocationInlineFormSet(prefix='location_item_set')
            context['image_items'] = ImageInlineFormSet(prefix='image_item_set')
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset_detail = context['detail_items']
        formset_location = context['location_items']
        formset_image = context['image_items']
        form.instance.user = self.request.user
        form.instance.status = 'Active'
        if form.is_valid() and formset_detail.is_valid() and formset_location.is_valid() and formset_image.is_valid():
            self.object = form.save()
            formset_detail.instance = self.object
            formset_detail.save()
            formset_location.instance = self.object
            formset_location.save()
            images = formset_image.save(commit=False)
            for image in images:
                image.flat = self.object
                image.save()
            return super(FlatCreateView, self).form_valid(form)
        else:
            return self.form_invalid(form)


class FlatListView(FilterView):
    model = Flat
    template_name = 'flats.html'
    context_object_name = 'flats'
    paginate_by = 10
    filterset_class = FlatFilter

    def get_queryset(self, *args, **kwargs):
        location = self.request.GET.get('search')
        queryset = super().get_queryset(**kwargs)
        if location:
            queryset = queryset.filter(
                Q(location__icontains=location),
                Q(title__icontains=location)
            )
        return queryset


class FlatDetailView(DetailView):
    model = Flat
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message_form'] = MessageForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        message_form = MessageForm(request.POST)

        if message_form.is_valid():
            chat, created = Chat.objects.get_or_create(
                name=self.object.title,
                participants=self.request.user,
                admin = self.request.user
            )
            chat.participants.add(self.object.user)
            # Create and save the message
            message = message_form.save(commit=False)
            message.sender = self.request.user
            message.chat = chat
            message.save()

            return redirect(reverse('detail', kwargs={'pk': self.object.pk}))

        # If form is invalid, render the page with errors
        context = self.get_context_data(message_form=message_form)
        return self.render_to_response(context)


class FlatUpdateView(LoginRequiredMixin, UpdateView):
    model = Flat
    login_url = 'login'
    template_name = 'update.html'
    form_class = UpdateFlatForm
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super(FlatUpdateView, self).get_context_data(**kwargs)
        context['equipments'] = Equip.objects.filter(flat=self.object).values_list('id', flat=True)
        if self.request.POST:
            context['image_items'] = UpdateImageInlineFormSet(self.request.POST, prefix='image_item_set')
        else:
            context['image_items'] = UpdateImageInlineFormSet(prefix='image_item_set')
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset_image = context['image_items']
        self.object = form.save()
        if self.object.id != None:
            if form.is_valid() and formset_image.is_valid():
                formset_image.instance = self.object
                formset_image.save()
                return super(FlatUpdateView, self).form_valid(form)
            else:
                return self.form_invalid(form)


class FlatDetailUpdateView(LoginRequiredMixin, UpdateView):
    model = FlatDetail
    template_name = 'update_detail.html'
    form_class = DetailUpdateForm
    context_object_name = 'detail'
    login_url = 'login'
    success_url = reverse_lazy("my_ads")


class FlatLocationUpdateView(LoginRequiredMixin, UpdateView):
    model = FlatLocation
    template_name = 'update_location.html'
    form_class = UpdateLocationForm
    context_object_name = 'location'
    login_url = 'login'
    success_url = reverse_lazy("my_ads")


class FlatImageUpdateView(LoginRequiredMixin, UpdateView):
    model = Flat
    template_name = 'update_image.html'
    form_class = ImageUpdateForm
    login_url = 'login'
    success_url = reverse_lazy("home")


class MyFlatListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Flat
    template_name = 'my_ads.html'
    context_object_name = 'flats'

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        queryset = super().get_queryset(**kwargs)
        queryset = queryset.filter(user=user)
        return queryset
