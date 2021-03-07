
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about1),
    path('tours', views.tours1),
    path('contact', views.contact1)
]