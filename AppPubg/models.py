from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    job = models.CharField(max_length=20)
    range = models.CharField(max_length=20)

    def __str__(self):
        return f" Jugador: {self.name} - Trabajo: {self.job} - Rango: {self.range}"

# ------------------------------------------------------------------------------------------------

class Maps(models.Model):
    name = models.CharField(max_length=20)
    size = models.IntegerField()
    rework = models.BooleanField()

    def __str__(self):
        return f" Mapa: {self.name} - Tamaño: {self.size} bloques "

# ------------------------------------------------------------------------------------------------

class Vehicle(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    speed = models.IntegerField()

    def __str__(self):
        return f" Vehiculo: {self.name} - Velocidad Maximo: {self.speed} Km/h - Tipo: {self.type}"

# ------------------------------------------------------------------------------------------------

class Equipment(models.Model):
    name = models.CharField(max_length=20)
    tier = models.IntegerField()
    reducedamage = models.BooleanField()

    def __str__(self):
        return f"Equipp: {self.name} - Nivel: {self.tier} - Reduccion de daño: {self.reducedamage}"

# ------------------------------------------------------------------------------------------------

class Weapons(models.Model):
    name = models.CharField(max_length=20)
    bullets = models.IntegerField()
    attachment = models.IntegerField()
    image = models.CharField(max_length=255,null=True)

    def __str__(self):
        return f" Arma: {self.name} - Tipo de Bala: {self.bullets} mm. - Accesorios: {self.attachment}"

# ------------------------------------------------------------------------------------------------

class Throwable(models.Model):
    name = models.CharField(max_length=20)
    damage = models.IntegerField()
    weight = models.IntegerField()

    def __str__(self):
        return f" Tipo: {self.name} - Daño: {self.damage} - Peso: {self.weight} gr. "