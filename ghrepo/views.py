from django.shortcuts import render

# Create your views here.
def github_repo(request):
    """set up our Github Repoview"""
    return render(request, 'ghrepo/gh-repo.html')
