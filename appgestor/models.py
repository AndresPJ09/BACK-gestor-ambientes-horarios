from time import localtime
from django.db import models
from django.contrib.auth.hashers import check_password
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import pre_save
from django.dispatch import receiver


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


class TipoVinculacion(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=180)
    descripcion = models.TextField(max_length=180)
    estado = models.BooleanField()
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'TipoVinculacion'


class Instructor(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    foto = models.BinaryField(null=True, blank=True)
    identificacion = models.CharField(max_length=10, unique=True, null=False, blank=False)
    tipo_vinculacion_id = models.ForeignKey(TipoVinculacion, on_delete=models.CASCADE, null=True)
    especialidad = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField()
    hora_ingreso = models.TimeField()
    hora_egreso = models.TimeField()
    horas_asignadas = models.IntegerField(
             default=0, 
        validators=[
            MinValueValidator(1), 
            MaxValueValidator(6)
        ]
    )
    estado = models.BooleanField()
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'Instructor'


class NivelFormacion(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=250)
    duracion = models.CharField(max_length=100)
    estado = models.BooleanField()
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'NivelFormacion'
        
        
from django.db import models

class Programa(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=100)
    nivel_formacion_id = models.ForeignKey(NivelFormacion, on_delete=models.CASCADE)
    estado = models.BooleanField()
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'Programa'


class Ambiente(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField(
             default=0, 
        validators=[
            MinValueValidator(20), 
            MaxValueValidator(40)
        ]
    )
    estado = models.BooleanField()
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'Ambiente'


class Periodo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    ano = models.IntegerField(
             default=0, 
        validators=[ 
            MinValueValidator(2025), 
            MaxValueValidator(2027)
        ]
    )
    estado = models.BooleanField()
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'Periodo'

####################################
#                O                 #   
####################################


class Competencia(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=20, null=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    estado = models.BooleanField()
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'Competencia'
        

class ResultadoAprendizaje(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField(max_length=250)
    est_ideal_evaluacion = models.CharField(max_length=20)
    competencia_id = models.ForeignKey(Competencia, on_delete=models.CASCADE)
    estado = models.BooleanField()
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'ResultadoAprendizaje'


class Proyecto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    jornada_tecncia = models.CharField(max_length=20)
    estado = models.BooleanField()
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'Proyecto'
        
        
class Fase(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, max_length=250)
    estado = models.BooleanField()
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'Fase'
        

class Ficha(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=20, unique=True)
    programa_id = models.ForeignKey(Programa, on_delete = models.CASCADE, null=True)
    proyecto_id = models.ForeignKey(Proyecto, on_delete = models.CASCADE, null=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    fin_lectiva = models.DateField()
    cupo = models.IntegerField(
             default=0, 
        validators=[
            MinValueValidator(20), 
            MaxValueValidator(40)
        ]
    )
    numero_semanas = models.IntegerField(editable=False, null=True, blank=True)
    #estado = models.BooleanField()
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Ficha {self.codigo}"
    
    def calcular_numero_semanas(self):
        """Calcula la diferencia en semanas entre fecha_inicio y fecha_fin"""
        if self.fecha_inicio and self.fecha_fin:
            return (self.fecha_fin - self.fecha_inicio).days // 7
        return 0  # Si no hay fechas, retorna 0

    class Meta:
        db_table = 'Ficha'

# 🚀 Mover la señal fuera de la clase para evitar el error
@receiver(pre_save, sender=Ficha)
def set_numero_semanas(sender, instance, **kwargs):
    instance.numero_semanas = instance.calcular_numero_semanas()



class ConsolidadoAmbiente(models.Model):
    id = models.AutoField(primary_key=True)
    ficha_id = models.ForeignKey(Ficha, on_delete = models.CASCADE, null=True)
    ambiente_id = models.ForeignKey(Ambiente, on_delete = models.CASCADE, null=True)
    observaciones = models.TextField(blank=True, max_length=255)
    estado = models.BooleanField()
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'ConsolidadoAmbiente'
        
from django.db import models

class Horario(models.Model):
    id = models.AutoField(primary_key=True)
    usuario_id = models.ForeignKey(Usuario, on_delete = models.CASCADE, null=True)
    ficha_id = models.ForeignKey(Ficha, on_delete = models.CASCADE, null=True)
    ambiente_id = models.ForeignKey(Ambiente, on_delete = models.CASCADE, null=True)
    periodo_id = models.ForeignKey(Periodo, on_delete = models.CASCADE, null=True)
    instructor_id = models.ForeignKey(Instructor, on_delete = models.CASCADE)
    
    jornada_programada = models.CharField(max_length=255)
    fecha_inicio_hora_ingreso = models.DateTimeField()
    fecha_fin_hora_egreso = models.DateTimeField()
    horas = models.IntegerField()
    validacion = models.CharField(max_length=255)
    observaciones = models.TextField(blank=True, max_length=255)
    
    estado = models.BooleanField()
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'Horario'
        
    def calcular_horas(self):
        """Calcula la diferencia en horas como un número entero (redondeando hacia abajo)."""
        if self.fecha_inicio_hora_ingreso and self.fecha_fin_hora_egreso:
            diferencia = localtime(self.fecha_fin_hora_egreso) - localtime(self.fecha_inicio_hora_ingreso)
            return diferencia.total_seconds() // 3600  # División entera para obtener solo las horas completas
        return 0  # Si no hay fechas, devolver el valor por defecto
    
    @receiver(pre_save, sender=Ficha)
    def set_horas(sender, instance, **kwargs):
        instance.horas = instance.calcular_horas()


class InstructorHorario(models.Model):
    id = models.AutoField(primary_key=True)
    dia = models.TextField(blank=True, max_length=20, null=True)
    horario_id = models.ForeignKey(Horario, on_delete = models.CASCADE, null=True)
    instructor_id = models.ForeignKey(Instructor, on_delete = models.CASCADE, null=True)
    observaciones = models.TextField(blank=True, max_length=255)
    estado = models.BooleanField()
    fechaCreo = models.DateTimeField(auto_now_add=True)
    fechaModifico = models.DateTimeField(auto_now=True)
    fechaElimino = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'InstructorHorario'