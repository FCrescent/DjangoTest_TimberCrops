from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from ..models import NatStruct
from ..forms import NatStructForm

class NatStructListView(ListView):
    model = NatStruct
    template_name = 'nat_struct_list.html'
    context_object_name = 'nat_structs'

class NatStructCreateView(CreateView):
    model = NatStruct
    form_class = NatStructForm
    template_name = 'nat_struct_form.html'
    success_url = reverse_lazy('nat_struct_list')

class NatStructUpdateView(UpdateView):
    model = NatStruct
    form_class = NatStructForm
    template_name = 'nat_struct_form.html'
    success_url = reverse_lazy('nat_struct_list')

class NatStructDeleteView(DeleteView):
    model = NatStruct
    success_url = reverse_lazy('nat_struct_list')
