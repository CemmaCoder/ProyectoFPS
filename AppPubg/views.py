from django.shortcuts import render, HttpResponse
from AppPubg.models import *
from AppPubg.forms import *
from django.template import loader


def inicioView(request):
    plantilla = loader.get_template("AppPubg/inicio.html")
    documento = plantilla.render()
    return HttpResponse(documento)

def playerView(request):
    players = Player.objects.all()
    resultado = {"players": players}
    return render(request, "AppPubg/player.html", resultado)

def mapsView(request):
    maps = Maps.objects.all()
    resultado = {"maps": maps} 
    return render(request, "AppPubg/maps.html", resultado)

def vehiclesView(request):
    vehicle = Vehicle.objects.all()
    resultado = {"vehicle": vehicle}
    return render(request, "AppPubg/vehicle.html", resultado)

def equipamentView(request):
    equipament = Equipment.objects.all()
    resultado = {"equipament": equipament}
    return render(request, "AppPubg/equipament.html", resultado)

def weaponsView(request):
    weapons = Weapons.objects.all()
    resultado = {"weapons": weapons}
    return render(request, "AppPubg/weapons.html", resultado)

def weaponSearch(request):
    if request.GET['weapon']:
        weapon = request.GET['weapon']
        weaponResult = Weapons.objects.filter(name=weapon)
        return render(request, "AppPubg/weaponsResult.html", {'weapons': weaponResult})
    else:
        respuesta= f"No hay resultados"
    return HttpResponse(respuesta)


def throwableView(request):
    throwable = Throwable.objects.all()
    resultado = {"throwable": throwable}
    return render(request, "AppPubg/throwable.html", resultado)

def playerFormView(request):
    if request.method == "POST":
        miFormulario = playerForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            player = Player(name=informacion['name'],email=informacion['email'],job=informacion['job'],range=informacion['range'])
            player.save()
            return render(request, "AppPubg/inicio.html")
    else:
        miFormulario = playerForm()
    return render(request, "AppPubg/playerForm.html", {'miFormulario':miFormulario})

def vehicleFormView(request):
    if request.method == "POST":
        miFormulario = vehicleForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            vehicle = Vehicle(name=informacion['name'],type=informacion['type'],speed=informacion['speed'])
            vehicle.save()
            return render(request, "AppPubg/inicio.html")
    else:
        miFormulario = vehicleForm()
    return render(request, "AppPubg/vehicleForm.html", {'miFormulario':miFormulario})

def mapFormView(request):
    if request.method == "POST":
        miFormulario = mapForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            map = Maps(name=informacion['name'],size=informacion['size'],rework=informacion['rework'])
            map.save()
            return render(request, "AppPubg/inicio.html")
    else:
        miFormulario = mapForm()
    return render(request, "AppPubg/mapsForm.html", {'miFormulario':miFormulario})