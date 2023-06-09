from django import forms
from posts.models import PostModel


class PostsForm(forms.ModelForm):
    """A class with a description of the form fields, and on
    based on which model the form functions
    """

    comment = forms.CharField(
        label="Опишите ваше путешествие, почему оно так запомнилось:",
        widget=forms.Textarea(attrs={'class': 'form-control', 'cols': 30, 'rows': 7}),
        required=True
    )
    address = forms.CharField(
        label="Адрес местоположения:",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Адрес',}),
        required=True

    )
    title = forms.CharField(
        label="Название вашего путешествия:",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок',}),
        required=True

    )

    class Meta:
        model = PostModel
        fields = ('comment', 'address', 'title', 'coords', 'image_screen_url')
        widgets = {
            'coords': forms.HiddenInput(attrs={'hidden': True}),
            'image_screen_url': forms.HiddenInput(attrs={'hidden': True}),
        }