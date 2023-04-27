from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "username",
                'placeholder' : "Nombre Usuario"
            }
        )
    )

    password = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type' : "password",
                    'id' : "password1",
                    'placeholder' : "Contraseña"
                }
            )
        )

    class Meta:
        model=User
        field = ["username", "password"]

class UserCreationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "username",
                'placeholder' : "Nombre Usuario"
            }
        )
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "first_name",
                'placeholder' : "Nombre"
            }
        )
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "last_name",
                'placeholder' : "Apellido"
            }
        )
    )

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "email",
                'id' : "email",
                'placeholder' : "Correo Electronico"
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "password",
                'id' : "password1",
                'placeholder' : "Contraseña"
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "password",
                'id' : "password2",
                'placeholder' : "Confirme su contraseña"
            }
        )
    )

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]


class UpdatedForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "username",
                'placeholder' : "Nombre Usuario"
            }
        )
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "first_name",
                'placeholder' : "Nombre"
            }
        )
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "last_name",
                'placeholder' : "Apellido"
            }
        )
    )

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "email",
                'id' : "email",
                'placeholder' : "Correo Electronico"
            }
        )
    )

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]



from usuario.models import Profile

class ProfileForm(forms.ModelForm):

    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "number",
                'id' : "phone_number",
                'placeholder' : "Numero de telefono"
            }
        )
    )

    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "address",
                'placeholder' : "Direccion"
            }
        )
    )

    class Meta:
        model = Profile
        fields = ['phone_number', 'address']

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete':"off", 'type' : "password", 'placeholder': 'Contraseña actual'})
    )
    new_password1 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete':"off", 'type' : "password", 'placeholder': 'Nueva contraseña'})
    )
    new_password2 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete':"off", 'type' : "password", 'placeholder': 'Confirmar nueva contraseña'})
    )