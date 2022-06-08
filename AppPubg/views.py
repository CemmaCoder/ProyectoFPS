from django.shortcuts import render, HttpResponse
from AppPubg.models import *
from AppPubg.forms import *
from django.template import loader
import requests

def inicioView(request):
    plantilla = loader.get_template("AppPubg/inicio.html")
    documento = plantilla.render()
    return HttpResponse(documento)

def playerView(request):
    # players = Player.objects.all()
    # resultado = {"players": players}
    # return render(request, "AppPubg/player.html", resultado)
    steam = requests.get("https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=364CECF1F7CECC8D8D8F5013FCA3B33B&steamids=76561198863200608, 76561198062499870, 76561198071054304, 76561198811795700, 76561198013869375, 76561198029714945, 76561198089723168, 76561198315971014, 76561198008323121, 76561198855533446")     
    JSONresponse = steam.json()     
    templateResponse = {'data': JSONresponse['response']['players']}     
    return render(request, 'AppPubg/player.html', {"response": templateResponse})

def mapsView(request):
    maps = Maps.objects.all()
    resultado = {"maps": maps} 
    return render(request, "AppPubg/maps.html", resultado)

def vehiclesView(request):
    vehicle = Vehicle.objects.all()
    resultado = {"vehicle": vehicle}
    return render(request, "AppPubg/vehicle.html", resultado)

def equipamentView(request):
    equipament = Equipament.objects.all()
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

def consumableView(request):
    consumable = Consumable.objects.all()
    resultado = {"consumable": consumable}
    return render(request, "AppPubg/consumable.html", resultado)

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
    return render(request, "AppPubg/mapForm.html", {'miFormulario':miFormulario})

def equipamentFormView(request):
    if request.method == "POST":
        miFormulario = equipamentForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            equipament = Equipament(name=informacion['name'], tier=informacion['tier'], armor=informacion['armor'], reducedamage=informacion['reducedamage'])
            equipament.save
            return render(request, "AppPubg/inicio.html")
    else:
        miFormulario = equipamentForm()
    return render(request, "AppPubg/equipamentForm.html", {'miFormulario':miFormulario})

def throwableFormView(request):
    if request.method == 'POST':
        miFormulario = throwableForm(request.POST)
        if miFormulario.is_valid(): 
            informacion = miFormulario.cleaned_data
            throwable = Throwable(name=informacion['name'], damage=informacion['damage'], weight=informacion['weight'])
            throwable.save()
            return render(request, "AppPubg/inicio.html")
    else:
        miFormulario = throwableForm()
    return render(request, "AppPubg/throwableForm.html", {'miFormulario':miFormulario})

def consumableFormView(request):
    if request.method == 'POST':
        miFormulario = consumableForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            consumable = Consumable(name=informacion['name'], weight=informacion['weight'], health=informacion['health'],boost=informacion['boost'])
            consumable.save()
            return render(request, "AppPubg/inicio.html")
    else:
        miFormulario = consumableForm()
    return render(request, "AppPubg/consumableForm.html", {'miFormulario':miFormulario})

def weaponFormView(request):
    if request.method == 'POST':
        miFormulario = consumableForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            weapon = Weapons(name=informacion['name'],bullets=informacion['bullets'],attachment=informacion['attachment'],type=informacion['type'],damage=informacion['damage'])
            weapon.save()
            return render(request, "AppPubg/inicio.html")
    else:
        miFormulario = consumableForm()
    return render(request, "AppPubg/weaponForm.html", {'miFormulario':miFormulario})