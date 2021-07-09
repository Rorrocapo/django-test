from api.serializers import ClienteSerializer
from api.models import Persona
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PersonaClienteSerilizer, ClienteSerializer, PersonaUsuarioSerializer
from . models import Persona, Cliente, Usuario

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Lista de Clientes': '/list-client/',
        'Lista de Usuarios': '/list-users/',
        'Crear Cliente': '/create-client/',
        'Crear Usuarios': '/create-user/',
    }

    return Response(api_urls)

@api_view(['GET'])
def showClients(request):
    persona = Persona.objects.all()
    serializers = PersonaClienteSerilizer(persona, many = True)

    return Response(serializers.data)

@api_view(['GET'])
def showUsers(request):
    persona = Persona.objects.all()
    serializers = PersonaUsuarioSerializer(persona, many = True)

    return Response(serializers.data)

@api_view(['POST'])
def createClient(request):
    serializer = PersonaClienteSerilizer(data= request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def createUser(request):
    serializer = PersonaUsuarioSerializer(data= request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)