from django.shortcuts import render, redirect
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required, user_passes_test


def homePage(request):
    print(request.user.__dir__())
    return render(request, './posts/home.html', {})


def postsPage(request):
    return render(request, './posts/posts.html', {})


def logout_view(request):
    logout(request)
    return redirect('home')
