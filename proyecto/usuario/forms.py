from usuario.models import Profile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.forms.widgets import ClearableFileInput

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': "text",
                'id': "username",
                'placeholder': "Nombre Usuario",
                'autocomplete': "off"
            }
        )
    )

    password = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': "password",
                'id': "password1",
                'placeholder': "Contraseña",
                'autocomplete': "off"
            }
        )
    )

    class Meta:
        model = User
        field = ["username", "password"]


class UserCreationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': "text",
                'id': "username",
                'placeholder': "Nombre Usuario",
                'autocomplete': "off"
            }
        )
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': "text",
                'id': "first_name",
                'placeholder': "Nombre",
                'autocomplete': "off"
            }
        )
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': "text",
                'id': "last_name",
                'placeholder': "Apellido",
                'autocomplete': "off"
            }
        )
    )

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': "email",
                'id': "email",
                'placeholder': "Correo Electronico",
                'autocomplete': "off"
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': "password",
                'id': "password1",
                'placeholder': "Contraseña",
                'autocomplete': "off"
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': "password",
                'id': "password2",
                'placeholder': "Confirme su contraseña",
                'autocomplete': "off"
            }
        )
    )

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name",
                  "email", "password1", "password2"]


class UpdatedForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': "text",
                'id': "username",
                'placeholder': "Nombre Usuario",
                'autocomplete': "off"
            }
        )
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': "text",
                'id': "first_name",
                'placeholder': "Nombre",
                'autocomplete': "off"
            }
        )
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': "text",
                'id': "last_name",
                'placeholder': "Apellido",
                'autocomplete': "off"
            }
        )
    )

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': "email",
                'id': "email",
                'placeholder': "Correo Electronico",
                'autocomplete': "off"
            }
        )
    )

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]


class ProfileForm(forms.ModelForm):

    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': "number",
                'id': "phone_number",
                'placeholder': "Numero de telefono",
                'autocomplete': "off"
            }
        )
    )

    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': "text",
                'id': "address",
                'placeholder': "Direccion",
                'autocomplete': "off"
            }
        )
    )

    image = forms.ImageField(
        widget=ClearableFileInput(attrs={
            'class': 'form-control'
        }),
        required=False
    )

    class Meta:
        model = Profile
        fields = ['phone_number', 'address', 'image']


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': "off",
                               'type': "password", 'placeholder': 'Contraseña actual'})
    )
    new_password1 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': "off",
                               'type': "password", 'placeholder': 'Nueva contraseña'})
    )
    new_password2 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': "off",
                               'type': "password", 'placeholder': 'Confirmar nueva contraseña'})
    )
