from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView
from django_filters.views import FilterView

from .filter import FlatFilter
from .forms import FlatForm, ImageInlineFormSet, LocationInlineFormSet
from .models import Flat

User = get_user_model()


def home(request):
    flats = Flat.objects.order_by('-created_at')
    return render(request, 'home.html', {'flats': flats})


class FlatCreateView(LoginRequiredMixin, CreateView):
    template_name = 'create.html'
    model = Flat
    form_class = FlatForm
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super(FlatCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['location_items'] = LocationInlineFormSet(self.request.POST, prefix='location_item_set')
            context['image_items'] = ImageInlineFormSet(self.request.POST, prefix='image_item_set')
        else:
            context['location_items'] = LocationInlineFormSet(prefix='location_item_set')
            context['image_items'] = ImageInlineFormSet(prefix='image_item_set')
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset_location = context['location_items']
        formset_image = context['image_items']
        self.object = form.save()
        if self.object.id != None:
            if form.is_valid() and formset_location.is_valid() and formset_image.is_valid():
                formset_location.instance = self.object
                formset_location.save()
                formset_image.instance = self.object
                formset_image.save()
        return super().form_valid(form)


class FlatListView(FilterView):
    model = Flat
    template_name = 'flat.html'
    context_object_name = 'flats'
    paginate_by = 10
    filterset_class = FlatFilter

    def get_queryset(self, *args, **kwargs):
        location = self.request.GET.get('search')
        queryset = super().get_queryset(**kwargs)
        if location:
            queryset = queryset.filter(
                Q(title__icontains=location)
            )
        return queryset


class FlatDetailView(generic.DetailView):
    model = Flat
    template_name = 'detail.html'
