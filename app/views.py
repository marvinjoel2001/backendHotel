from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

from .models import Cliente, Habitacion, Reserva, Pago
from .serializers import ClienteSerializer, HabitacionSerializer, ReservaSerializer, PagoSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class HabitacionViewSet(viewsets.ModelViewSet):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer


class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        is_user_valid = True  # Variable para almacenar el resultado de verificación del usuario

        # Realiza aquí la lógica de verificación del usuario
        # Puedes usar cualquier condición o método que desees para determinar si el usuario es válido

        if user.is_active:  # Ejemplo: verifica si el usuario está activo
            is_user_valid = True
        else:
            is_user_valid = False

        return Response({'is_user_valid': is_user_valid}, status=status.HTTP_200_OK)
