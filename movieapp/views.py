import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response

from movieapp.models import Movie
from movieapp.serializers import MovieSerializer
import urllib.request
import urllib
import json
from urllib.parse import quote


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'Movie List': '/movie-list/',
        'Movie Update/Delete': '/movie-edit/<pk>/',
        'Movie Create': '/movie-create/',
    }
    return Response(api_urls)


class MovieList(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    name = 'movie-list'
    filter_backends = [DjangoFilterBackend]
    filter_fields = (
        'id',
        'released_year',
        'genre',
        'ratings',
    )


@api_view(['GET', 'POST'])
def movie_create(request):
    if request.method == 'GET':
        movie_list = Movie.objects.all()
        serialize = MovieSerializer(movie_list, many=True)
        return Response(serialize.data)
    if request.method == 'POST':
        if request.data != {}:
            serialize = MovieSerializer(data=request.data)
            if serialize.is_valid():
                serialize.save()
                return Response(serialize.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_edit(request, pk):
    # if request.method == 'GET':
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response("Record not found !", status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serialize = MovieSerializer(movie)
        return Response(serialize.data)
    if request.method == 'PUT':
        if request.data != {}:
            serialize = MovieSerializer(movie, data=request.data)
            if serialize.is_valid():
                serialize.save()
                return Response(serialize.data)
            else:
                return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'DELETE':
        movie.delete()
        return Response("Record Deleted Successfully !", status=status.HTTP_204_NO_CONTENT)






