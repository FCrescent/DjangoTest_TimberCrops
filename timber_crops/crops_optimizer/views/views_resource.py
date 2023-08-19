from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from ..models import Resource
from ..forms import ResourceForm

class ResourceListView(ListView):
    model = Resource
    template_name = 'resource_list.html'
    context_object_name = 'resource'

class ResourceCreateView(CreateView):
    model = Resource
    form_class = ResourceForm
    template_name = 'resource_form.html'
    success_url = reverse_lazy('resource_list')

class ResourceUpdateView(UpdateView):
    model = Resource
    form_class = ResourceForm
    template_name = 'resource_form.html'
    success_url = reverse_lazy('resource_list')

class ResourceDeleteView(DeleteView):
    model = Resource
    success_url = reverse_lazy('resource_list')
