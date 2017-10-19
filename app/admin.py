from django.contrib import admin
from .models import Photo, Person, Vote

admin.site.register(Photo)
admin.site.register(Person)
admin.site.register(Vote)