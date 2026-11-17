"""
URL configuration for tienda_musica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from . import views

app_name = 'instrumentos'

urlpatterns = [
    path('', views.InstrumentoListView.as_view(), name='lista'),
    path('instrumento/<int:pk>/', views.InstrumentoDetailView.as_view(), name='detalle'),
    path('nuevo/', views.InstrumentoCreateView.as_view(), name='crear'),
    path('instrumento/<int:pk>/editar/', views.InstrumentoUpdateView.as_view(), name='editar'),
    path('instrumento/<int:pk>/eliminar/', views.InstrumentoDeleteView.as_view(), name='eliminar'),
]