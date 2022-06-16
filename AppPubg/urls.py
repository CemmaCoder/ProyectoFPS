from django.urls import path
from AppPubg.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", inicioView,name='home'),
    path("player/", playerView,name='player'),
    path("equipament/", equipamentView,name='equipament'),
    path("weapons/", weaponsView,name='weapon'),
    path("consumable/", consumableView,name='consumable'),
    path("throwable/", throwableView,name='throwable'),
    path("vehicles/", vehiclesView,name='vehicle'),
    path("maps/", mapsView,name='maps'),
    # ----------------------------
    path("playerForm/", playerFormView,name='playerForm'),
    path("equipamentForm/", equipamentFormView,name='equipamentForm'),
    path("weaponForm/", weaponFormView,name='weaponForm'),
    path("weaponResult/", weaponSearch,name='weaponResult'),
    path("consumableForm/", consumableFormView,name='consumableForm'),
    path("throwableForm/", throwableFormView,name='throwableForm'),
    path("vehicleForm/", vehicleFormView,name='vehicleForm'),
    path("mapForm/", mapFormView,name='mapForm'),
    # ----------------------------
    path("register", register_request, name='register'),
    path("login", login_request, name='login'),
    path("logout", LogoutView.as_view(template_name= 'AppPubg/logout.html'), name='logout'),
    ]