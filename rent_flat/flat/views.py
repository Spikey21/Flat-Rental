from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import FlatForm, ImageInlineFormSet, LocationInlineFormSet
from .models import Flat

User = get_user_model()


def home(request):

    return render(request, 'home.html', )


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


    # def get(self, request, *args, **kwargs):
    #     """
    #     Handles GET requests and instantiates blank versions of the form
    #     and its inline formsets.
    #     """
    #     self.object = None
    #     form_class = self.get_form_class()
    #     form = self.get_form(form_class)
    #     image_form = ImageInlineFormSet()
    #     location_form = LocationInlineFormSet()
    #     return self.render_to_response(
    #         self.get_context_data(form=form,image_form=image_form, location_form=location_form))
    #
    # def post(self, request, *args, **kwargs):
    #     """
    #     Handles POST requests, instantiating a form instance and its inline
    #     formsets with the passed POST variables and then checking them for
    #     validity.
    #     """
    #     self.object = None
    #     form_class = self.get_form_class()
    #     form = self.get_form(form_class)
    #     image_form = ImageInlineFormSet(self.request.POST)
    #     location_form = LocationInlineFormSet(self.request.POST)
    #     if form.is_valid() and image_form.is_valid() and location_form.is_valid():
    #         return self.form_valid(form, image_form, location_form)
    #     else:
    #         return self.form_invalid(form, image_form, location_form)
    #
    # def form_valid(self, form, image_form, location_form):
    #     """
    #     Called if all forms are valid. Creates a Recipe instance along with
    #     associated Ingredients and Instructions and then redirects to a
    #     success page.
    #     """
    #     form.instance.user = self.request.user
    #     self.object = form.save()
    #     image_form.instance = self.object
    #     image_form.save()
    #     location_form.instance = self.object
    #     location_form.save()
    #     return HttpResponseRedirect(self.get_success_url())
    #
    # def form_invalid(self, form, image_form, location_form):
    #     """
    #     Called if a form is invalid. Re-renders the context data with the
    #     data-filled forms and errors.
    #     """
    #     return self.render_to_response(self.get_context_data(form=form, image_form=image_form, location_form=location_form))