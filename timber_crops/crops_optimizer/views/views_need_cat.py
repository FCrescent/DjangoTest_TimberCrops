from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from ..models import NeedCat
from ..forms import NeedCatForm

class NeedCatListView(ListView):
    model = NeedCat
    template_name = 'need_cat_list.html'
    context_object_name = 'need_cat'

class NeedCatCreateView(CreateView):
    model = NeedCat
    form_class = NeedCatForm
    # fields = ['name']
    template_name = 'need_cat_form.html'
    success_url = reverse_lazy('need_cat_list')

class NeedCatUpdateView(UpdateView):
    model = NeedCat
    fields = ['name']
    template_name = 'need_cat_form.html'
    success_url = reverse_lazy('need_cat_list')

class NeedCatDeleteView(DeleteView):
    model = NeedCat
    success_url = reverse_lazy('need_cat_list')
