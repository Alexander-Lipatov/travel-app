from django.urls import path
from .views import homePage, postsPage, logout_view

urlpatterns = [
    path('', homePage, name='home'),
    path('my-travel/', postsPage, name='posts'),
    path('logout/', logout_view, name='logout')

]
