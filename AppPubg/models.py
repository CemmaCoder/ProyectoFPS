from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    job = models.CharField(max_length=20)
    range = models.CharField(max_length=20)
    steam = models.CharField(max_length=255,null=True)

    def __str__(self):
        return f"  Jugador: {self.name} - Rol: {self.job} - Rango: {self.range}"

# ------------------------------------------------------------------------------------------------

class Maps(models.Model):
    name = models.CharField(max_length=20)
    size = models.IntegerField()
    rework = models.BooleanField()
    link = models.CharField(max_length=255,null=True)

    def __str__(self):
        return f" {self.name} - Tamaño: {self.size} bloques "

# ------------------------------------------------------------------------------------------------

class Vehicle(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    speed = models.IntegerField()
    ocupant = models.IntegerField(null=True)
    health = models.IntegerField(null=True)
    image = models.CharField(max_length= 255,null=True)

    def __str__(self):
        return f" {self.name} - Capacidad: {self.ocupant} pasajeros - Velocidad Maxima: {self.speed} Km/h - Vida: {self.health} - Tipo: {self.type}"

# ------------------------------------------------------------------------------------------------

class Equipament(models.Model):
    name = models.CharField(max_length=20)
    tier = models.IntegerField()
    armor = models.IntegerField(null=True)
    reducedamage = models.IntegerField()
    capacity = models.IntegerField(null=True)
    image = models.CharField(max_length=255,null=True)

    def __str__(self):
        return f"{self.name} - Nivel: {self.tier} Armadura: {self.armor} - Reduccion de daño: {self.reducedamage}% - Capacidad: {self.capacity}"

# ------------------------------------------------------------------------------------------------

class Weapons(models.Model):
    name = models.CharField(max_length=20)
    bullets = models.IntegerField()
    attachment = models.IntegerField()
    type = models.CharField(max_length=20,null=True)
    damage = models.IntegerField(null=True)
    image = models.CharField(max_length=255,null=True)

    def __str__(self):
        return f" Arma: {self.name} - Tipo: {self.type} - Calibre: {self.bullets}mm. - Daño: {self.damage} - Accesorios: Maximo {self.attachment}"

# ------------------------------------------------------------------------------------------------

class Throwable(models.Model):
    name = models.CharField(max_length=20)
    damage = models.IntegerField()
    weight = models.IntegerField()
    image = models.CharField(max_length=255,null=True)

    def __str__(self):
        return f" Nombre: {self.name} - Daño: {self.damage} - Peso: {self.weight} gr. "

# ------------------------------------------------------------------------------------------------

class Consumable(models.Model):
    name = models.CharField(max_length=20)
    weight = models.IntegerField()
    health = models.IntegerField()
    boost = models.IntegerField()
    castTime = models.IntegerField(null=True)
    image = models.CharField(max_length=255,null=True)

    def __str__(self):
        return f" {self.name} - Peso: {self.weight} gr. - Curacion: {self.health}/100 - Aceleracion: {self.boost} instantaneo - Uso: {self.castTime} segundos."