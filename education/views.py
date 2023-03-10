from django.shortcuts import render


def education(request):
    """set up our education and knowledge view"""
    return render(request, 'education / education.html')
