
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UserModel
from django import forms

class CrearUsuarioFormulario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = ["password1", "password2", "username", "email"]
        help_texts = {k: "" for k in fields}