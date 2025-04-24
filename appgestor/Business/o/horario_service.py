from appgestor.Business.base_service import BaseService
from appgestor.Entity.Dao.o.horario_dao import HorarioDAO
from appgestor.Entity.Dto.o.horario_dto import HorarioDTO
from appgestor.models import Ambiente, ConsolidadoAmbiente, ConsolidadoHorario, Ficha, Horario, Instructor, InstructorHorario, Periodo, Usuario
from django.db import transaction, connection
from django.core.exceptions import ObjectDoesNotExist

# Este helper lo puedes tener al inicio del archivo o antes de la clase

# Mapea automáticamente el estado booleano a estado de ConsolidadoAmbiente
def map_estado_consolidado(estado_bool):
    if estado_bool in [True, 'true', '1', 1]:
        return '1'  # Disponible
    elif estado_bool in [False, 'false', '0', 0]:
        return '3'  # Inactivo
    return '2'  # Default a Ocupado si es ambiguo

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
        estado = data.get('estado', True) 
        if isinstance(estado, str):  
            estado = estado.lower() == 'true' 
        
        # ✅ Convertir `activo` en booleano manualmente
        if not bool(ambiente.estado):
            raise ValueError("No se puede asignar un horario a un ambiente inactivo.")
        if not bool(ficha.estado):
            raise ValueError("No se puede asignar un horario a una ficha inactiva.")
        if not bool(periodo.estado):
            raise ValueError("No se puede asignar un horario a un periodo inactivo.")
        if not bool(instructor.estado):
            raise ValueError("No se puede asignar un horario a un instructor inactivo.")
        
        # Verificar si el instructor ya tiene un horario en el mismo día y jornada
        existe_horario_instructor = Horario.objects.filter(
            instructor_id=instructor,
            dia=data.get('dia'),
            jornada_programada=data.get('jornada_programada')   
        ).exists()

        if existe_horario_instructor:
            raise ValueError("Este instructor ya tiene un horario asignado en ese día y jornada.")
        
        # Verificar si ya existe un horario en ese ambiente para ese día y jornada
        ambiente_ocupado = Horario.objects.filter(
            ambiente_id=ambiente,
            dia=data.get('dia'),
            jornada_programada=data.get('jornada_programada')
        ).exists()

        if ambiente_ocupado:
            raise ValueError("Este ambiente ya está ocupado para ese día y jornada.")

        
        horario = Horario.objects.create(
            usuario_id=usuario,  
            ficha_id=ficha,  
            ambiente_id=ambiente,  
            periodo_id=periodo,  
            instructor_id=instructor,  
            dia=data.get('dia'),
            jornada_programada=data.get('jornada_programada'),
            fecha_inicio_hora_ingreso=data.get('fecha_inicio_hora_ingreso'),
            fecha_fin_hora_egreso=data.get('fecha_fin_hora_egreso'),
            horas=data.get('horas'),
            validacion=data.get('validacion'),
            observaciones=data.get('observaciones'),
            estado=estado 
        )
        InstructorHorario.objects.create(
            horario_id=horario,
            instructor_id=instructor,
            observaciones=data.get('observaciones'),
            estado=horario.estado
        )
        
        # Guardar solo los ID en ConsolidadoAmbiente
        estado_consolidado = map_estado_consolidado(estado)
        ConsolidadoAmbiente.objects.create(
            ambiente_id=ambiente,
            horario_id=horario,
            estado=estado_consolidado
        )

        # Guardar solo los ID en ConsolidadoHorario
        ConsolidadoHorario.objects.create(
            horario_id=horario,
            estado=horario.estado
        )
        return horario
    

    @staticmethod
    @transaction.atomic
    def update_horario_con_instructor(horario_id, data):
        try:
            horario = Horario.objects.get(id=horario_id)
            
            estado = data.get('estado', horario.estado) 
            if isinstance(estado, str):
                estado = estado.lower() == 'true'
                
            if 'ficha_id' in data:
                ficha = Ficha.objects.get(id=data['ficha_id'])
            if not ficha.estado:
                raise ValueError("No se puede asignar una ficha inactiva.")
            horario.ficha_id = ficha
            
            if 'usuario_id' in data:
                usuario = Usuario.objects.get(id=data['usuario_id'])
                horario.usuario_id = usuario
        
            if 'ambiente_id' in data:
                ambiente = Ambiente.objects.get(id=data['ambiente_id'])
            if not ambiente.estado:
                raise ValueError("No se puede asignar un ambiente inactivo.")
            horario.ambiente_id = ambiente
         
            if 'periodo_id' in data:
                periodo = Periodo.objects.get(id=data['periodo_id'])
            if not periodo.estado:
                raise ValueError("No se puede asignar un período inactivo.")
            horario.periodo_id = periodo
        
            if 'instructor_id' in data:
                instructor = Instructor.objects.get(id=data['instructor_id'])
            if not instructor.estado:
                raise ValueError("No se puede asignar un instructor inactivo.")
            horario.instructor_id = instructor

            # Verificar si el instructor ya tiene un horario en el mismo día y jornada
            existe_horario_instructor = Horario.objects.filter(
                instructor_id=instructor,
                dia=data.get('dia'),
                jornada_programada=data.get('jornada_programada')   
            ).exists()

            if existe_horario_instructor:
                raise ValueError("Este instructor ya tiene un horario asignado en ese día y jornada.")
        
            # Verificar si ya existe un horario en ese ambiente para ese día y jornada
            ambiente_ocupado = Horario.objects.filter(
                ambiente_id=ambiente,
                dia=data.get('dia'),
                jornada_programada=data.get('jornada_programada')
            ).exists()

            if ambiente_ocupado:
                raise ValueError("Este ambiente ya está ocupado para ese día y jornada.")

            # Actualizar los datos del horario
            horario.dia = data.get('dia', horario.dia)
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
            
            
            # Actualizar ConsolidadoAmbiente (solo guardar IDs)
            consolidado_ambiente, created = ConsolidadoAmbiente.objects.get_or_create(horario_id=horario)
            consolidado_ambiente.ambiente_id = horario.ambiente_id
            consolidado_ambiente.horario_id = horario # Pasar la instancia, no el ID
            estado_consolidado = map_estado_consolidado(horario.estado)
            consolidado_ambiente.estado = estado_consolidado
            consolidado_ambiente.save()
            
            # **Actualizar ConsolidadoHorario (solo guardar IDs)**
            consolidado_horario, created = ConsolidadoHorario.objects.get_or_create(horario_id=horario)
            consolidado_horario.horario_id = horario # Pasar la instancia, no el ID
            consolidado_horario.estado = horario.estado  
            consolidado_horario.save()
            
            return horario

        except ObjectDoesNotExist:
            raise ValueError("Horario no encontrado")
        except ValueError as e:
            raise ValueError(f"Error de validación: {str(e)}")
        except Exception as e:
            raise ValueError(f"Error inesperado: {str(e)}")
        
        
        
        
    