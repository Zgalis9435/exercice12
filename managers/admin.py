from django.contrib import admin

# Register your models here.
from .models import genere,nameManager,movieTitle,summary

admin.site.register(genere)
admin.site.register(nameManager)
admin.site.register(movieTitle)
admin.site.register(summary)