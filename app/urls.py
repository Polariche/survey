from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.photo_survey, name='photo_survey')
]