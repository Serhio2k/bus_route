from django.contrib import messages
from django.shortcuts import render, redirect
from routes.forms import RouteForm
from routes.utils import get_routes


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
        return render(request, 'routes/create.html', context)

    else:
        messages.error(request, 'Неможливо зберегти неіснуючий маршрут')
        return redirect('/')
