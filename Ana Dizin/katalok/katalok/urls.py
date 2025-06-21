from django.contrib import admin
from django.urls import path,include

#http://127.0.0.1:8000/admin

urlpatterns = [
    path('', include('pages.urls')),
    path('movies/', include('movies.urls')),
    path('user/', include('user.urls')),
    path('admin/', admin.site.urls),
    path('', include('hesaplar.urls')),

]
