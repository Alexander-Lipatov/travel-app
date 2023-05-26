from django.urls import path
from .views import homePage, postsPage

urlpatterns = [
    path('', homePage, name='home'),
    path('my-travel/', postsPage, name='posts')
]
