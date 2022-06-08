from django import forms

class playerForm(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=30)
    job = forms.CharField(max_length=20)
    range = forms.CharField(max_length=20)

# ------------------------------------------------------------------------------------------------
class mapForm(forms.Form):
    name = forms.CharField(max_length=20)
    size = forms.IntegerField()
    rework = forms.BooleanField()

# ------------------------------------------------------------------------------------------------
class vehicleForm(forms.Form):
    name = forms.CharField(max_length=20)
    type = forms.CharField(max_length=20)
    speed = forms.IntegerField()
    ocupant = forms.IntegerField()
    health = forms.IntegerField()

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
class throwableForm(forms.Form):
    name = forms.CharField(max_length=20)
    damage = forms.IntegerField()
    weight = forms.IntegerField()

# ------------------------------------------------------------------------------------------------

class consumableForm(forms.Form):
    name = forms.CharField(max_length=20)
    weight = forms.IntegerField()
    health = forms.IntegerField()
    boost = forms.IntegerField()
    castTime = forms.IntegerField()