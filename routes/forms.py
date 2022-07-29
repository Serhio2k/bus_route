from django import forms

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
