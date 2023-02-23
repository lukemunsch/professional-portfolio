from django.urls import path

from . import views

urlpatterns = [
    path('', views.github_repo, name='github-repo')
]
