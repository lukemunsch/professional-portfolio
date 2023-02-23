from django.urls import path

from . import views

urlpatterns = [
    path('', views.hobbies, name='hobbies')
]
