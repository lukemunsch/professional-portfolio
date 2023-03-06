from django.shortcuts import render

# Create your views here.
def hobbies(request):
    """set up our hobbies and interest view"""
    return render(request, 'hobbies/hobbies.html')
