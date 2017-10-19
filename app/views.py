from django.shortcuts import render
from .models import Photo
from survey import settings

# Create your views here.

def photo_survey(request, univcode):
	photos = Photo.objects.all()
	return render(request, 'index.html', 
		{'univcode': univcode,
		'photos': photos, 
		'totalphotos': len(photos),
		'names': ' '.join([photo.filename for photo in photos])})
