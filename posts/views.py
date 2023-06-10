from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView

from .models import PostModel
from .forms import PostsForm


class HomePageView(ListView):
    """This view class is responsible for 
    displaying the main page and the list of publications
    """

    template_name = './posts/home.html'
    model = PostModel

    def get_template_names(self):
        if self.request.user.is_authenticated:
            self.template_name = './posts/posts.html'
        return super().get_template_names()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            # Получение публикаций только для аутентифицированного пользователя
            posts = PostModel.objects.filter(owner=self.request.user)
            context['posts'] = posts.order_by('-created_date')
        return context


class CreatePostView(LoginRequiredMixin, CreateView):
    """This representation class responds to
    for displaying the travel creation form
    """

    model = PostModel
    form_class = PostsForm
    template_name = './posts/create-post.html'
    success_url = '/'
    login_url = '/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


def logout_view(request):
    """This presentation method is responsible 
    for the user logging out of the system
    """

    logout(request)
    return redirect('home')
