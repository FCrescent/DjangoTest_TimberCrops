from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from ..models import NatStructCat
from ..forms import NatStructCatForm

class NatStructCatListView(ListView):
    model = NatStructCat
    template_name = 'nat_struct_cat_list.html'
    context_object_name = 'nat_struct_categories'

class NatStructCatCreateView(CreateView):
    model = NatStructCat
    form_class = NatStructCatForm
    template_name = 'nat_struct_cat_form.html'
    success_url = reverse_lazy('nat_struct_cat_list')

class NatStructCatUpdateView(UpdateView):
    model = NatStructCat
    form_class = NatStructCatForm
    # fields = ['name']
    template_name = 'nat_struct_cat_form.html'
    success_url = reverse_lazy('nat_struct_cat_list')

class NatStructCatDeleteView(DeleteView):
    model = NatStructCat
    success_url = reverse_lazy('nat_struct_cat_list')
