from django.shortcuts import render


def hobbies(request):
    """set up our hobbies and interest view"""
    return render(request, 'hobbies / hobbies.html')
