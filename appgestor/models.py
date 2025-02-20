from django.db import models
from django.contrib.auth.hashers import check_password

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
