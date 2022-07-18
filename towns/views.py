from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from towns.forms import TownForm
from towns.models import Town

__all__ = (
    'home',
    'TownDetailView',
    'TownCreateView',
    'TownUpdateView',
    'TownDeleteView',
    'TownListView',
)


def home(request, pk=None):
    if request.method == 'POST':
        form = TownForm(request.POST)
        if form.is_valid():
            form.save()
    # if pk:
    #     town = get_object_or_404(Town, id=pk)
    #     print(town)
    #     context = {'object': town}
    #     return render(request, 'towns/detail.html', context)
    form = TownForm()
    qs = Town.objects.all()
    lst = Paginator(qs, 2)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj': page_obj, 'form': form}
    return render(request, 'towns/home.html', context)


class TownDetailView(DetailView):
    queryset = Town.objects.all()
    template_name = 'towns/detail.html'


class TownCreateView(SuccessMessageMixin, CreateView):
    model = Town
    form_class = TownForm
    template_name = 'towns/create.html'
    success_url = reverse_lazy('towns:home')
    success_message = 'Місто успішно створено'


class TownUpdateView(SuccessMessageMixin, UpdateView):
    model = Town
    form_class = TownForm
    template_name = 'towns/update.html'
    success_url = reverse_lazy('towns:home')
    success_message = 'Місто успішно відредоговано'


class TownDeleteView(DeleteView):
    model = Town
    # template_name = 'towns/delete.html'
    success_url = reverse_lazy('towns:home')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Місто успішно видалено')
        return self.delete(request, *args, **kwargs)


class TownListView(ListView):
    paginate_by = 5
    model = Town
    template_name = 'towns/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = TownForm()
        context['form'] = form
        return context
