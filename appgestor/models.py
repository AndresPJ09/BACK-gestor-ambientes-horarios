from django.db import models
from django.contrib.auth.hashers import check_password
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Modulo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    icono = models.TextField(blank=True, null=True)
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'Modulo'

class Vista(models.Model):
    id = models.AutoField(primary_key=True)
    modulo_id = models.ForeignKey(Modulo, on_delete = models.CASCADE)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    icono = models.TextField(blank=True, null=True)
    ruta = models.TextField(blank=True, null=True)
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'Vista'

class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'Rol'
     
class RolVista(models.Model):
    id = models.AutoField(primary_key=True)
    rol_id = models.ForeignKey(Rol, on_delete= models.CASCADE)
    vista_id = models.ForeignKey(Vista, on_delete= models.CASCADE)
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        db_table = 'RolVista'

class TipoDocumento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'TipoDocumento'

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    correo = models.EmailField(unique=True)
    contrasena = models.TextField(blank=True, null=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    tipoDocumento = models.ForeignKey(TipoDocumento, on_delete = models.CASCADE, null=True)
    documento = models.CharField(max_length=10, unique=True, null=False, blank=False)
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)

    def verificar_contasena(self, contrasena):
        return check_password(contrasena, self.contrasena)
    
    class Meta: 
        db_table = 'Usuario'

class UsuarioRol(models.Model):
    id = models.AutoField(primary_key=True)
    usuario_id =models.ForeignKey(Usuario, on_delete=models.CASCADE)
    rol_id = models.ForeignKey(Rol, on_delete=models.CASCADE)
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'UsuarioRol'

class RecuperarContrasena(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10)
    expiracion = models.DateTimeField(blank=True, null=True)
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    usado = models.BooleanField(default=False)

    class Meta:
        db_table = 'RecuperarContrasena'

####################################
#                p                 #   
####################################

class Instructor(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    foto = models.BinaryField()
    identificacion = models.BigIntegerField(unique=True)
    tipo_contrato = models.CharField(max_length=255)
    especialidad = models.CharField(max_length=255)
    correo = models.EmailField(unique=True)
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField()
    hora_ingreso = models.TimeField()
    hora_egreso = models.TimeField()
    horas_asignadas = models.IntegerField()
    estado = models.BooleanField()
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'instructor'


class NivelFormacion(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=255)
    duracion = models.DurationField()
    estado = models.BooleanField()
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'nivel_formacion'


class Ambiente(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=255)
    capacidad = models.IntegerField(
             default=0, 
        validators=[
            MinValueValidator(0), 
            MaxValueValidator(40)
        ]
    )
    estado = models.BooleanField()
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'ambiente'


class Periodo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    ano = models.IntegerField()
    estado = models.BooleanField()
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'periodo'




####################################
#                O                 #   
####################################