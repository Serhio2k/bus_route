from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView

from buses.models import Bus
from routes.forms import RouteForm, RouteModelForm
from routes.models import Route
from routes.utils import get_routes
from towns.models import Town


def home(request):
    form = RouteForm()
    return render(request, 'routes/home.html', {'form': form})


def bus_routes(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            try:
                context = get_routes(request, form)
            except ValueError as err:
                messages.error(request, err)
                return render(request, 'routes/home.html', {'form': form})
            return render(request, 'routes/home.html', context)
        return render(request, 'routes/home.html', {'form': form})
    else:
        form = RouteForm()
        messages.error(request, 'Нічого немає для пошуку')
        return render(request, 'routes/home.html', {'form': form})


def add_routes(request):
    if request.method == 'POST':
        context = {}
        data = request.POST
        if data:
            total_time = int(data['total_time'])
            from_town_id = int(data['from_town'])
            to_town_id = int(data['to_town'])
            buses = data['buses'].split(',')
            buses_lst = [int(b) for b in buses if b.isdigit()]
            qs = Bus.objects.filter(id__in=buses_lst).select_related('from_town', 'to_town')
            towns = Town.objects.filter(id__in=[from_town_id, to_town_id]).in_bulk()
            form = RouteModelForm(
                initial={'from_town': towns[from_town_id],
                         'to_town': towns[to_town_id],
                         'travel_times': total_time,
                         'buses': qs,
                         }
            )
            context['form'] = form
        return render(request, 'routes/create.html', context)

    else:
        messages.error(request, 'Неможливо зберегти не існуючий маршрут')
        return redirect('/')


def save_routes(request):
    if request.method == 'POST':
        form = RouteModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Маршрут збережено')
            return redirect('/')
        return render(request, 'routes/create.html', {'form': form})

    else:
        messages.error(request, 'Неможливо зберегти не існуючий маршрут')
        return redirect('/')


class RouteListView(ListView):
    paginate_by = 10
    model = Route
    template_name = 'routes/list.html'


class RouteDetailView(DetailView):
    queryset = Route.objects.all()
    template_name = 'routes/detail.html'


class RouteDeleteView(LoginRequiredMixin, DeleteView):
    model = Route
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Маршрут успішно видалено')
        return self.delete(request, *args, **kwargs)
