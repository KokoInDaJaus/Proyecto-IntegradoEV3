from django.db import models

class Farmacia(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    correo = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'farmacia'


class Moto(models.Model):
    patente = models.CharField(max_length=10)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField(db_column="anio", verbose_name="año")
    tipo = models.CharField(max_length=20)
    disponible = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.patente}"
    
    class Meta:
        db_table = 'moto'

class Motorista(models.Model):
    LICENCIA_OPCIONES = [
        ('C1', 'Clase C1'),
        ('C2', 'Clase C2'),
        ('C3', 'Clase C3'),
    ]

    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)
    telefono = models.CharField(max_length=15)
    correo = models.CharField(max_length=100)
    licencia = models.CharField(max_length=20, choices=LICENCIA_OPCIONES)  # 👈 cambio aquí
    estado = models.CharField(max_length=20)
    moto = models.ForeignKey(Moto, on_delete=models.SET_NULL, null=True, blank=True, db_column='moto_id')
    farmacia = models.ForeignKey(Farmacia, on_delete=models.CASCADE, db_column='farmacia_id')
    fecha_ingreso = models.DateField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'motorista'
