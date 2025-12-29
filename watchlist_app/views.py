from django.shortcuts import render
from watchlist_app.models import Movie
from django.http import JsonResponse


def movie_list(request):
    movies = Movie.objects.all()  # queryset
    movies_dict = movies.values()  # Python dict
    movies_list = list(movies_dict)  # Json

    data = {"movies": movies_list}

    return JsonResponse(data)


def movie_detail(request, pk):
    movie = Movie.objects.get(id=pk)
    data = {
        "name": movie.name,
        "description": movie.description,
        "active": movie.active,
    }

    return JsonResponse(data)
