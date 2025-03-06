from appgestor.Business.base_service import BaseService
from appgestor.Entity.Dao.o.horario_dao import HorarioDAO
from appgestor.Entity.Dto.o.horario_dto import HorarioDTO
from appgestor.models import Ambiente, Ficha, Horario, Instructor, InstructorHorario, Periodo, Usuario
from django.db import transaction, connection
from django.core.exceptions import ObjectDoesNotExist

class HorarioService(BaseService):
    dao=HorarioDAO
    model=HorarioDTO
    
    @staticmethod
    @transaction.atomic
    def crear_horario_con_instructor(data):
        usuario = Usuario.objects.get(id=data.get('usuario_id'))
        ficha = Ficha.objects.get(id=data.get('ficha_id'))
        ambiente = Ambiente.objects.get(id=data.get('ambiente_id'))
        periodo = Periodo.objects.get(id=data.get('periodo_id'))
        instructor = Instructor.objects.get(id=data.get('instructor_id'))
        estado = data.get('estado', True)  # Si no se envía, por defecto es True
        if isinstance(estado, str):  
            estado = estado.lower() == 'true'  # Convierte "true"/"false" en booleano


        horario = Horario.objects.create(
            usuario_id=usuario,  
            ficha_id=ficha,  
            ambiente_id=ambiente,  
            periodo_id=periodo,  
            instructor_id=instructor,  
            jornada_programada=data.get('jornada_programada'),
            fecha_inicio_hora_ingreso=data.get('fecha_inicio_hora_ingreso'),
            fecha_fin_hora_egreso=data.get('fecha_fin_hora_egreso'),
            horas=data.get('horas', 0),
            validacion=data.get('validacion'),
            observaciones=data.get('observaciones'),
            estado=estado 
        )

        InstructorHorario.objects.create(
            horario_id=horario,
            instructor_id=instructor,  
            observaciones=data.get('observaciones'),
            estado=True
        )

        return horario
    
    
    
    @staticmethod
    @transaction.atomic
    def update_horario_con_instructor(horario_id, data):
        try:
            horario = Horario.objects.get(id=horario_id)
            
            
                 # Convertir valores si es necesario
            estado = data.get('estado', horario.estado)  # Si no se envía, conserva el valor actual
            if isinstance(estado, str):
             estado = estado.lower() == 'true'  # Convierte "true"/"false" a booleano

            # Actualizar los datos del horario
            horario.jornada_programada = data.get('jornada_programada', horario.jornada_programada)
            horario.fecha_inicio_hora_ingreso = data.get('fecha_inicio_hora_ingreso', horario.fecha_inicio_hora_ingreso)
            horario.fecha_fin_hora_egreso = data.get('fecha_fin_hora_egreso', horario.fecha_fin_hora_egreso)
            horario.horas = data.get('horas', horario.horas)
            horario.validacion = data.get('validacion', horario.validacion)
            horario.observaciones = data.get('observaciones', horario.observaciones)
            horario.estado = estado

            # Verificar si se envió un nuevo instructor
            if 'instructor_id' in data:
                nuevo_instructor = Instructor.objects.get(id=data['instructor_id'])
                horario.instructor_id = nuevo_instructor  # Actualizar el instructor

            horario.save()

            # Actualizar InstructorHorario
            instructor_horario, created = InstructorHorario.objects.get_or_create(horario_id=horario)
            instructor_horario.instructor_id = horario.instructor_id
            instructor_horario.observaciones = horario.observaciones
            instructor_horario.estado = horario.estado
            instructor_horario.save()

            return horario

        except ObjectDoesNotExist:
            raise ValueError("Horario no encontrado")
    