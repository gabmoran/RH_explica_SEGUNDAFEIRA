from django.contrib import admin
from django.urls import path
from landing_rh import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.retornar_home),
    path('cadastro', views.retornar_cadastro),
]
