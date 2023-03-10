from django.shortcuts import render


def contact(request):
    """set up our contact page view"""
    return render(request, 'contact / contact_me.html')
