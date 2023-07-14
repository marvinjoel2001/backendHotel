from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, HabitacionViewSet, ReservaViewSet, PagoViewSet, CustomAuthToken

router = DefaultRouter()
router.register('clientes', ClienteViewSet, basename='cliente')
router.register('habitaciones', HabitacionViewSet, basename='habitacion')
router.register('reservas', ReservaViewSet, basename='reserva')
router.register('pagos', PagoViewSet, basename='pago')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', CustomAuthToken.as_view(), name='api_login'),
]
