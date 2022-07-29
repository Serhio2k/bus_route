from django import forms

from towns.models import Town


class TownForm(forms.ModelForm):
    name = forms.CharField(label='Місто', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                        'placeholder': 'Введіть назву міста'}))

    class Meta:
        model = Town
        fields = ('name',)
