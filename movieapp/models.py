from django.db import models

# Create your models here.

RATINGS = (
    ('5', '5 Star'),
    ('4', '4 Star'),
    ('3', '3 Star'),
    ('2', '2 Star'),
    ('1', '1 Star'),
)


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField()
    ratings = models.CharField(choices=RATINGS, max_length=1)
    genre = models.ManyToManyField(Genre)
    released_year = models.DateField()

    def __str__(self):
        return self.title
