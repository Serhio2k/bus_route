from django.core.exceptions import ValidationError
from django.db import models

from towns.models import Town


class Bus(models.Model):
    name = models.CharField(max_length=50, unique=True,
                            verbose_name='Номер автобуса')
    travel_time = models.PositiveSmallIntegerField(verbose_name='Час в дорозі')
    from_town = models.ForeignKey(Town, on_delete=models.CASCADE,
                                  related_name='from_town_set',
                                  verbose_name='З якого міста')

    to_town = models.ForeignKey('towns.Town', on_delete=models.CASCADE,
                                related_name='to_town_set',
                                verbose_name='В яке місто')

    def __str__(self):
        return f'Автобус №{self.name} з міста {self.from_town}'

    class Meta:
        verbose_name = 'Автобус'
        verbose_name_plural = 'Автобуси'
        ordering = ['travel_time']

    def clean(self):
        if self.from_town == self.to_town:
            raise ValidationError('Змініть місто прибуття')
        qs = Bus.objects.filter(
            from_town=self.from_town, to_town=self.to_town,
            travel_time=self.travel_time).exclude(pk=self.pk)

        if qs.exists():
            raise ValidationError('Змініть час в дорозі')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


