from django.db import models
from django.db.models.fields.related import ForeignKey
from .choices import genero, tipo_telefono, estado_civil, roles
from phone_field import PhoneField

# Create your models here.
class Persona (models.Model):
    nombre_persona = models.CharField(max_length= 100)
    apellido_paterno = models.CharField(max_length= 100)
    apellido_materno = models.CharField(max_length= 100)
    tipo_telefono = models.CharField(max_length= 1, choices= tipo_telefono, default= 'H' )
    telefono_persona = PhoneField(help_text = 'Numero tel')

    class Meta:
        db_table = 'tbl_personas'

    def __str__(self):
        text = '{} {} {}'
        return text.format(self.nombre_persona, self.apellido_paterno, self.apellido_materno)

class Cliente (models.Model):
    persona = models.ForeignKey(Persona, related_name= 'cliente', on_delete= models.CASCADE)
    fecha_creacion = models.DateField()
    genero_cliente = models.CharField(max_length= 1, choices= genero, default= 'F')
    entidad_nacimiento = models.CharField(max_length= 100)
    curp_cliente = models.CharField(max_length= 100)
    rfc_cliente = models.CharField(max_length= 100)
    estado_civil = models.CharField(max_length= 1, choices= estado_civil, default= 'S')

    class Meta:
        db_table = 'tbl_clientes'

    def __str__(self):
        return self.rfc_cliente

class Usuario (models.Model):
    persona = models.ForeignKey(Persona, related_name= 'usuario', on_delete= models.CASCADE)
    nombre_usuario = models.CharField(max_length= 100)
    password_usuario = models.CharField(max_length=500)
    rfc_usuario = models.CharField(max_length= 100)
    fecha_alta = models.DateField()

    class Meta:
        db_table = 'tbl_usuarios'

    def __str__(self):
        return self.nombre_usuario

class Grupo (models.Model):
    folio_solicitud = models.CharField(max_length= 100)
    nombre_grupo = models.CharField(max_length= 100)
    usuario_captura = models.CharField(max_length= 100)
    usuario_coloca = models.CharField(max_length= 100)
    usuario_verifica = models.CharField(max_length= 100)
    fecha_creacion = models.DateField()
    monto_total = models.DecimalField(max_digits=20, decimal_places= 2)
    plazo_pago = models.IntegerField()
    plazos_forzosos = models.IntegerField()
    garantia_liquida = models.IntegerField()
    num_integrantes = models.IntegerField()

    class Meta:
        db_table = 'tbl_grupos'

    def __str__(self):
        return self.nombre_grupo

class ClienteHasGrupo  (models.Model):
    cliente = ForeignKey(Cliente, related_name= 'cliente', on_delete= models.CASCADE)
    grupo = ForeignKey(Grupo, related_name= 'grupo', on_delete= models.CASCADE)
    rol_grupo = models.CharField(max_length= 1, choices= roles, default= 'I')
    monto_aprobado = models.DecimalField(max_digits= 20, decimal_places= 2)
    monto_total_pagar = models.DecimalField(max_digits= 20, decimal_places= 2)

    class Meta:
        db_table = 'm_clientes_has_m_grupos'

    def __str__(self):
        text = 'Grupo {}, Cliente: {} {} {}'
        return text.format(self.grupo.nombre_grupo, self.cliente.persona.nombre_persona, self.cliente.persona.apellido_paterno, self.cliente.persona.apellido_materno)