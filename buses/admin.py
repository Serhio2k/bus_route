from django.contrib import admin

from buses.models import Bus


class BusAdmin(admin.ModelAdmin):
    class Meta:
        model = Bus

    list_display = ('name', 'from_town', 'to_town', 'travel_time')
    list_editable = ('travel_time',)


admin.site.register(Bus,BusAdmin)
