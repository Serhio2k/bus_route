from django import forms

from buses.models import Bus
from routes.models import Route
from towns.models import Town


class RouteForm(forms.Form):
    from_town = forms.ModelChoiceField(
        label='Звідки', queryset=Town.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control js-example-basic-single'}))

    to_town = forms.ModelChoiceField(
        label='Куди', queryset=Town.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control js-example-basic-single'}))

    towns = forms.ModelMultipleChoiceField(
        label='Через міста',
        queryset=Town.objects.all(),
        required=False,
        widget=forms.SelectMultiple(
            attrs={'class': 'form-control js-example-basic-multiple'})
    )
    travelling_time = forms.IntegerField(
        label='Час в дорозі',
        widget=forms.NumberInput(attrs={'class': 'form-control',
                                        'placeholder': 'Час в дорозі'}))


class RouteModelForm(forms.ModelForm):
    name = forms.CharField(label='Назва маршруту',
                           widget=forms.TextInput(
                               attrs={'class': 'form-control',
                                      'placeholder': 'Назва маршруту'}))
    from_town = forms.ModelChoiceField(
        queryset=Town.objects.all(),
        widget=forms.HiddenInput()
    )

    to_town = forms.ModelChoiceField(
        queryset=Town.objects.all(),
        widget=forms.HiddenInput()
    )

    buses = forms.ModelMultipleChoiceField(
        queryset=Bus.objects.all(),
        required=False,
        widget=forms.SelectMultiple(
            attrs={'class': 'form-control d-none'})
    )
    travel_times = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Route
        fields = '__all__'
