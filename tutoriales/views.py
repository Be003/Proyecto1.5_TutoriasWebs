from django.shortcuts import render
from tutoriales.models import Tutorial
# Create your views here.

def tutoriales(request):
    tutoriales = Tutorial.objects.all()
    return render(request, "tutoriales/tutoriales.html", {"tutoriales": tutoriales})

def whatsapp(request):
    return render(request, "tutoriales/whatsapp.html")

def youtube(request):
    return render(request, "tutoriales/youtube.html")