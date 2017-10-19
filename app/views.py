from django.shortcuts import render
from .models import Photo, Person
from survey import settings

# Create your views here.

def photo_survey(request, univcode):
	photos = Photo.objects.all()
	return render(request, 'index.html', 
		{'univcode': univcode,
		'studentcode': 0 if univcode == 'G' else len(Person.objects.filter(univ_code ='J')),
		'photos': photos, 
		'totalphotos': len(photos),
		'names': ' '.join([photo.filename for photo in photos])})
