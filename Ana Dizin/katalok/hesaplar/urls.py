from django.urls import path
from . import views

urlpatterns = [
    path('giris/', views.kullanici_giris, name='giris'),
    path('kayit/', views.kullanici_kayit, name='kayit'),
    path('cikis/', views.kullanici_cikis, name='cikis'),
]
