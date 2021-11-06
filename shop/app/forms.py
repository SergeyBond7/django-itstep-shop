from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label="Имя", widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Фамилия", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Подтверждение пароля", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label=False,
                               widget=forms.TextInput(
                                attrs={
                                    'class': 'fadeIn second',
                                    'id': 'login',
                                    'placeholder': "Логин",
                                    'name': "login",
                                    'type': "text"
                               }))

    password = forms.CharField(label=False,
                               widget=forms.PasswordInput
                               (attrs={
                                    'class': 'fadeIn third',
                                    'id': 'password',
                                    'placeholder': "Пароль",
                                    'name': "login",
                                    'type': "password"
                               }))

    class Meta:
        model = User
        fields = ('username', 'password1')


CHOICE_GENDER = ((1, 'Нова пошта'), (2, 'Укрпошта'))


class CheckoutContactForm(forms.Form):
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    delivery = forms.ChoiceField(required=True, choices=CHOICE_GENDER)