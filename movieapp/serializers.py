from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
import omdb
from .models import Movie


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
