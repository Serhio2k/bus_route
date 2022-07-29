from django.db import models

from towns.models import Town


class Route(models.Model):
    name = models.CharField(max_length=50, unique=True,
                            verbose_name='Назва маршрута')
    travel_times = models.PositiveSmallIntegerField(verbose_name='Загальний час в дорозі')
    from_town = models.ForeignKey(Town, on_delete=models.CASCADE,
                                  related_name='route_from_town_set',
                                  verbose_name='З якого міста')

    to_town = models.ForeignKey('towns.Town', on_delete=models.CASCADE,
                                related_name='route_to_town_set',
                                verbose_name='В яке місто')

    buses = models.ManyToManyField(
        'buses.Bus', verbose_name='Список автобусів')

    def __str__(self):
        return f'Маршрут {self.name} з міста {self.from_town}'

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршрути'
        ordering = ['travel_times']
