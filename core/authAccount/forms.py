from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.models import User
from django.forms import PasswordInput
from django.core import validators



class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                
                "class": "form-control",
                'autocomplete':'on'
            }
        ),
        validators=[
                validators.MinLengthValidator(4, message="El E-Mail es demasiado corto"),
				validators.RegexValidator('^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$', message="El E-Mail ingresado no es válido")
        ],
                error_messages={'required':'El campo E-Mail está vacío' }
        )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                
                "class": "form-control",
            }
        ))

#### Registro

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                
                "class": "form-control",
                'autocomplete':'on'
            }
        ),
        validators=[
                validators.MinLengthValidator(4, message="El E-Mail es demasiado corto"),
				validators.RegexValidator('^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$', message="El E-Mail ingresado no es válido")
        ],
                error_messages={'required':'El campo E-Mail está vacío' }
        )
    
        
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
### cambio de contraseña ###

class PasswordResetForm(PasswordResetForm):
    
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                
                "class": "form-control",
                'autocomplete':'on'
            }
        ),
        validators=[
                validators.MinLengthValidator(4, message="El E-Mail es demasiado corto"),
				validators.RegexValidator('^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$', message="El E-Mail ingresado no es válido")
        ],
                error_messages={'required':'El campo E-Mail está vacío' }
        )
        
    

    class Meta:
        model = User
        fields = ( 'email', )


class PasswordChangeForm(PasswordChangeForm):
        
    old_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                
                "class": "form-control"
            }
        ))
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                
                "class": "form-control"
            }
        ))
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ( 'old_password', 'new_password1', 'new_password2')
        

    