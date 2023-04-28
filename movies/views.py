from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe
from .models import Movie, Genre


API_KEY = "13e149d16bf61eaad0368a40a8a17771"


# Create your views here.
@require_safe
def index(request):
    # 전체 영화 목록 가져오기
    movies = Movie.objects.all()
    context = {"movies": movies}
    print(context)
    return render(request, "movies/index.html", context)


@require_safe
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {
        "movie": movie,
    }
    return render(request, "movies/detail.html", context)


@require_safe
def recommended(request):
    pass
