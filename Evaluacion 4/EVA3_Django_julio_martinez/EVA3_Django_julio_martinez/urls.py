from django.contrib import admin
from django.urls import path, include
from entretenimiento import views
from django.conf import settings
from django.views.static import serve
from django.urls import re_path
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clases/', views.clases, name='clases'),
    path('', views.home, name='home'),
    path('pago_exitoso/<int:transaccion_id>/', views.pago_exitoso, name='pago_exitoso'),
    path('reservar_clase/<int:clase_id>/', views.reservar_clase, name='reservar_clase'),
    path('servicio/', views.servicios, name='servicio'),
    path('reservar_servicio/<int:servicio_id>/', views.reservar_servicio, name='reservar_servicio'),
    path('comprobante_pago/', views.comprobante_pago, name='comprobante_pago'),

    path('', include('entretenimiento.urls'))

]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]