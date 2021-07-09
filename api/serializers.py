from django.db import models
from rest_framework import fields, serializers
from .models import Persona, Cliente, Usuario

class PersonaSerializer (serializers.ModelSerializer):
    class Meta:
        model =  Persona
        fields = [
            'id',
            'nombre_persona',
            'apellido_paterno',
            'apellido_materno',
            'tipo_telefono',
            'telefono_persona',
        ]

class ClienteSerializer (serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = [
            'id',
            'fecha_creacion',
            'genero_cliente',
            'entidad_nacimiento',
            'curp_cliente',
            'rfc_cliente',
            'estado_civil',
        ]

class UsuarioSerializer (serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'id',
            'nombre_usuario',
            'password_usuario',
            'rfc_usuario',
            'fecha_alta',
        ]

class PersonaClienteSerilizer (serializers.ModelSerializer):
    cliente = ClienteSerializer(many =  True)

    class Meta:
        model = Persona
        fields = [
            'id',
            'nombre_persona',
            'apellido_paterno',
            'apellido_materno',
            'tipo_telefono',
            'telefono_persona',
            'cliente',
        ]

    def create(self, validated_data):
        cliente_data = validated_data.pop('cliente')
        persona = Persona.objects.create(**validated_data)
        for client_data in cliente_data:
            Cliente.objects.create(persona=persona, **client_data)
        return persona

class PersonaUsuarioSerializer (serializers.ModelSerializer):
    usuario = UsuarioSerializer(many = True)

    class Meta:
        model = Persona
        fields = [
            'id',
            'nombre_persona',
            'apellido_paterno',
            'apellido_materno',
            'tipo_telefono',
            'telefono_persona',
            'usuario',
        ]

    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        persona = Persona.objects.create(**validated_data)
        for user_data in usuario_data:
            Usuario.objects.create(persona=persona, **user_data)
        return persona