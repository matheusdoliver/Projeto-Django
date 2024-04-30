from django.contrib import admin
from django.urls import path
from registro.views import fogete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', fogete),
]
