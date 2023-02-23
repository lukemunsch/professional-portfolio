from django.shortcuts import render, get_object_or_404

from .models import Project

# Create your views here.

def all_projects(request):
    """set up page for resume viewing"""
    project = Project.objects.all()

    context = {
        'project': project,
    }

    return render(request, 'resume/resume.html', context)

def project_details(request, project_id):
    """set up the link to view individual projects"""
    project = Project.objects.all()
    chosen_project = project.filter(pk=project_id)
    context = {
        'project': project,
        'chosen_project': chosen_project,
    }
    return render(request, 'resume/project-details.html', context)
