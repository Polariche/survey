from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^submit$', views.submit, name='submit'),
	url(r'^result$', views.create_sheet, name='create_sheet'),
    url(r'^(?P<univcode>\w+)$', views.photo_survey, name='photo_survey')
]