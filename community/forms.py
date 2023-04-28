from django import forms
from .models import Review, Comment
from movies.models import Movie


class ReviewForm(forms.ModelForm):
    try:
        choices = list(map(lambda x: (x.title, x.title), Movie.objects.all()))
    except:
        choices = []
    movie_title = forms.ChoiceField(choices=choices)

    class Meta:
        model = Review
        fields = ["title", "movie_title", "rank", "content"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["review", "user"]
