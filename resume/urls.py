from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_projects, name='resume'),
    path('<int:project_id>/', views.project_details, name='project_details')
]
