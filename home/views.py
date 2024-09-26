from django.shortcuts import render

from resume.models import Project


def index(request):
    """set up our index view"""
    projects = Project.objects.filter(home_display=True)

    context = {
        'projects': projects,
    }

    return render(request, 'home/index.html', context)
