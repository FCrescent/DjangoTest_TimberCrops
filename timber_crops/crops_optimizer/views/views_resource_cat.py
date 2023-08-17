from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from ..models import ResourceCat
from ..forms import ResourceCatForm

class ResourceCatListView(ListView):
    model = ResourceCat
    template_name = 'resource_cat_list.html'
    context_object_name = 'resource_cat'

class ResourceCatCreateView(CreateView):
    model = ResourceCat
    form_class = ResourceCatForm
    # fields = ['name']
    template_name = 'resource_cat_form.html'
    success_url = reverse_lazy('resource_cat_list')

class ResourceCatUpdateView(UpdateView):
    model = ResourceCat
    fields = ['name']
    template_name = 'resource_cat_form.html'
    success_url = reverse_lazy('resource_cat_list')

class ResourceCatDeleteView(DeleteView):
    model = ResourceCat
    success_url = reverse_lazy('resource_cat_list')
