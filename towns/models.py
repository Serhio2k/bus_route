from django.db import models
from django.urls import reverse


class Town(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Місто')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Місто'
        verbose_name_plural = 'Міста'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('towns:detail', kwargs={'pk': self.pk})
