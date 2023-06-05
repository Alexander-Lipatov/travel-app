from django.urls import path
from .views import HomePageView, logout_view, CreatePostView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('create/', CreatePostView.as_view(), name='create-post'),
    path('logout/', logout_view, name='logout')

]
