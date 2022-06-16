from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class playerForm(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=30)
    job = forms.CharField(max_length=20)
    range = forms.CharField(max_length=20)


# ------------------------------------------------------------------------------------------------
class equipamentForm(forms.Form):
    name = forms.CharField(max_length=20)
    tier = forms.IntegerField()
    armor = forms.IntegerField()
    reducedamage = forms.IntegerField()


# ------------------------------------------------------------------------------------------------
class weaponForm(forms.Form):
    name = forms.CharField(max_length=20)
    bullets = forms.IntegerField()
    attachment = forms.IntegerField()
    type = forms.CharField(max_length=20)
    damage = forms.IntegerField()


# ------------------------------------------------------------------------------------------------
class consumableForm(forms.Form):
    name = forms.CharField(max_length=20)
    weight = forms.IntegerField()
    health = forms.IntegerField()
    boost = forms.IntegerField()
    castTime = forms.IntegerField()


# ------------------------------------------------------------------------------------------------
class throwableForm(forms.Form):
    name = forms.CharField(max_length=20)
    damage = forms.IntegerField()
    weight = forms.IntegerField()


# ------------------------------------------------------------------------------------------------
class vehicleForm(forms.Form):
    name = forms.CharField(max_length=20)
    type = forms.CharField(max_length=20)
    speed = forms.IntegerField()
    ocupant = forms.IntegerField()
    health = forms.IntegerField()


# ------------------------------------------------------------------------------------------------
class mapForm(forms.Form):
    name = forms.CharField(max_length=20)
    size = forms.IntegerField()
    rework = forms.BooleanField()


# ------------------------------------------------------------------------------------------------
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label= "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label= "Reingrese la contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}


# ------------------------------------------------------------------------------------------------









