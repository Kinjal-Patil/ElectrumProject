from django.db import models

# Create your models here.

RATINGS = (
    ('5', '5 Star'),
    ('4', '4 Star'),
    ('3', '3 Star'),
    ('2', '2 Star'),
    ('1', '1 Star'),
)


class Movie(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField()
    ratings = models.CharField(choices=RATINGS, max_length=1)
    genre = models.CharField(max_length=255)
    released_year = models.DateField()

    def __str__(self):
        return self.title
