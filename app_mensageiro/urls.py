from django.urls import path
from django.conf.urls.static import static
from site_rondon import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mensageiro', views.mensageiro, name='mensageiro'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)
