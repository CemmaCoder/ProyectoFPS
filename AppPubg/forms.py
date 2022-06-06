from django import forms

class playerForm(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=30)
    job = forms.CharField(max_length=20)
    range = forms.CharField(max_length=20)

class vehicleForm(forms.Form):
    name = forms.CharField(max_length=20)
    type = forms.CharField(max_length=20)
    speed = forms.IntegerField()

class mapForm(forms.Form):
    name = forms.CharField(max_length=20)
    size = forms.IntegerField()
    rework = forms.BooleanField()