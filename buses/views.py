from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView, CreateView, UpdateView, DeleteView, ListView)
from buses.forms import BusForm
from buses.models import Bus

__all__ = (
    'home',
    'BusListView',
    'BusDetailView',
    'BusCreateView',
    'BusUpdateView',
    'BusDeleteView',
)


def home(request):
    qs = Bus.objects.all()
    lst = Paginator(qs, 5)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj': page_obj, }
    return render(request, 'buses/home.html', context)


class BusListView(ListView):
    paginate_by = 5
    model = Bus
    template_name = 'buses/home.html'


class BusDetailView(DetailView):
    queryset = Bus.objects.all()
    template_name = 'buses/detail.html'


class BusCreateView(SuccessMessageMixin,LoginRequiredMixin, CreateView):
    model = Bus
    form_class = BusForm
    template_name = 'buses/create.html'
    success_url = reverse_lazy('buses:home')
    success_message = 'Автобус успішно створено'


class BusUpdateView(SuccessMessageMixin,LoginRequiredMixin, UpdateView):
    model = Bus
    form_class = BusForm
    template_name = 'buses/update.html'
    success_url = reverse_lazy('buses:home')
    success_message = 'Автобус успішно відредаговано'


class BusDeleteView(LoginRequiredMixin,DeleteView):
    model = Bus
    # template_name = 'buses/delete.html'
    success_url = reverse_lazy('buses:home')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Автобус успішно видалено')
        return self.delete(request, *args, **kwargs)


