from django.shortcuts import render

# Create your views here.
def hobbies(request):
    """set up our index view"""
    return render(request, 'hobbies/hobbies.html')
