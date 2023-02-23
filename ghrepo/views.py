from django.shortcuts import render

# Create your views here.
def github_repo(request):
    """set up our index view"""
    return render(request, 'ghrepo/gh-repo.html')
