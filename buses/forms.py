from django import forms
from buses.models import Bus
from towns.models import Town


class BusForm(forms.ModelForm):
    name = forms.CharField(label='Номер автобуса',
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Введіть назву автобуса'}))

    travel_time = forms.IntegerField(label='Час в дорозі',
                                     widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                     'placeholder': 'Час в дорозі'}))

    from_town = forms.ModelChoiceField(label='Звідки', queryset=Town.objects.all(),
                                       widget=forms.Select(attrs={'class': 'form-control'}))

    to_town = forms.ModelChoiceField(label='Куди', queryset=Town.objects.all(),
                                     widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Bus
        fields = '__all__'
