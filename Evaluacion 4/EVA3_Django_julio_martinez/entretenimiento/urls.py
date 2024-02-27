from rest_framework import routers
from .api import ClaseViewSet, ServicioViewSet, TransaccionViewSet

router = routers.DefaultRouter()

router.register('api/clase', ClaseViewSet, 'entretenimiento')
router.register('api/servicio', ServicioViewSet, 'entretenimiento')
router.register('api/transaccion', TransaccionViewSet, 'entretenimiento')



urlpatterns = router.urls