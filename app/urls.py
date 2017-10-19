from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<univcode>\w+)$', views.photo_survey, name='photo_survey')
]