from django.contrib import admin

# Register your models here.
from .models import movie,ticket
admin.site.register(movie)
admin.site.register(ticket)