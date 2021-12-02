from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.tutoriales, name="Tutoriales"),
    path('whatsapp',views.whatsapp, name="Whatsapp"),
    path('youtube',views.youtube, name="Youtube"),
]

