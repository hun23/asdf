from django.shortcuts import render
from django.views.decorators.http import require_safe



API_KEY = '13e149d16bf61eaad0368a40a8a17771'


# Create your views here.
@require_safe
def index(request):
    pass


@require_safe
def detail(request, movie_pk):
    pass


@require_safe
def recommended(request):
    pass
