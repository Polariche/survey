from django.shortcuts import render
from .models import Photo
from survey import settings

# Create your views here.

def photo_survey(request):
	photos = Photo.objects.all()
	imagepath = settings.PHOTO_ROOT
	return render(request, 'index.html', {'imagepath': imagepath, 'photos': photos})
