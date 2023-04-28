from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:movie_pk>/", views.detail, name="detail"),
    # path("recommended/<int:genre_pk>", views.recommended, name="recommended"),
    path("recommended/", views.recommended, name="recommended"),
    path("genre/<int:genre_id>/", views.GenreDetail, name="GenreDetail"),
]
