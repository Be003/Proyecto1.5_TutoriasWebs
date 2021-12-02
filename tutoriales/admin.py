from django.contrib import admin
from .models import Tutorial

# Register your models here.
class TutorialAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Tutorial, TutorialAdmin)
