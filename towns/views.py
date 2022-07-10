from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from towns.models import Town

__all__ = (
    'home',
    'TownDetailView'
)


def home(request, pk=None):
    # if pk:
    #     town = get_object_or_404(Town, id=pk)
    #     print(town)
    #     context = {'object': town}
    #     return render(request, 'towns/detail.html', context)

    qs = Town.objects.order_by('name')
    context = {'objects_list': qs}
    return render(request, 'towns/home.html', context)


class TownDetailView(DetailView):
    queryset = Town.objects.all()
    template_name = 'towns/detail.html'
