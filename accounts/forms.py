from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import check_password

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(label='login',
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Введіть login'}))
    password = forms.CharField(label='password',
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Введіть passsword'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            qs = User.objects.filter(username=username)
            if not qs.exists():
                raise forms.ValidationError('Такого користувача не існує')
            if not check_password(password, qs[0].password):
                raise forms.ValidationError('Не вірний пароль')
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Даний користувчач не активний')
            return super().clean(*args, **kwargs)


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Логін',
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Введіть Логін'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Введіть пароль'}))
    password2 = forms.CharField(label='Повторіть пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Повторіть пароль'}))

    class Meta:
        model = User
        fields = ('username',)

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('Паролі не співпадають')
        return data['password2']
