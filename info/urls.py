from django.urls import path
from . import views

urlpatterns = [
    path('animal/<int:animal_id>/',views.animal)
]

