
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('consulta/', include('consulta.urls')),
    path('paciente/', include('paciente.urls')),
    path('feedback/', include('feedback_consulta.urls')),
    path('feedback/', include('feedback_plataforma.urls')),
    path('', include('home.urls')),
]
