from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe
from .models import Movie, Genre
import heapq

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
    user = request.user
    if user.is_authenticated:
        # 10개 영화 추천
        recommneded_movies_priority_queue = []
        all_genres = set(Genre.objects.all())
        all_movie_ranking = Movie.objects.all().order_by("vote_average")
        all_movie_visited = [False] * len(all_movie_ranking)
        # 1. 좋아요한 영화의 장르 받기
        liked_reviews = user.like_reviews.all()
        print(liked_reviews)
        liked_movie_genres = set()
        for lr in liked_reviews:
            try:
                mv = Movie.objects.get(title=lr.movie_title)
                print(mv)
                gnrs = mv.genres.all()
                for gnr in gnrs:
                    liked_movie_genres.add(gnr)
            except:
                print("no matching mv title")
        print(f"liked: {liked_movie_genres}")
        # 2. 각 장르별 영화 추천
        # 3. 각 장르별 별점 기준 추천
        # 4. 각 장르 겹치는 수가 많을수록 먼저 추천
        if len(liked_movie_genres) == 0:
            liked_movie_genres = all_genres
        for idx, mv in enumerate(all_movie_ranking):
            # 해당 mv의 generes.all과 liked_genres와의 우선순위 구하기
            priority = len(liked_movie_genres.intersection(mv.genres.all()))
            if all_movie_visited[idx] == False:
                all_movie_visited[idx] = True
                heapq.heappush(recommneded_movies_priority_queue, (-priority, idx))
        print(recommneded_movies_priority_queue)
        cnt = 0
        recommneded_movies = []
        while cnt < 10:  # 우선순위 큐에서 10개만 뽑기
            popped = heapq.heappop(recommneded_movies_priority_queue)
            recommneded_movies.append(all_movie_ranking[popped[1]])
            cnt += 1
        print(recommneded_movies)
        context = {"recommneded_movies": recommneded_movies}
        return render(request, "movies/recommended.html", context)
    return redirect("moives:index")


@require_safe
def GenreDetail(request, genre_id):
    genre = Genre.objects.get(pk=genre_id)
    movies = genre.movie_set.all()
    context = {
        "movies": movies,
    }
    return render(request, "movies/index.html", context)
