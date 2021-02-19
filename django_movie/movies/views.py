from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from .models import Movie


class MoviesView(View):
    """Список фильмов"""