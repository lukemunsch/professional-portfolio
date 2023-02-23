from django.shortcuts import render

# Create your views here.
def education(request):
    """set up our index view"""
    return render(request, 'education/education.html')
