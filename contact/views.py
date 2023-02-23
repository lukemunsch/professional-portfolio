from django.shortcuts import render

# Create your views here.
def contact(request):
    """set up our index view"""
    return render(request, 'contact/contact_me.html')
