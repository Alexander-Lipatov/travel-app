from django.shortcuts import render

# Create your views here.


def homePage(request):
    return render(request, './posts/home.html', {})


def postsPage(request):
    return render(request, './posts/posts.html', {})
