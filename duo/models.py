from django.contrib.postgres.search import SearchVectorField
from django.db import models


class Sentence(models.Model):

    japanese = models.TextField()

    english = models.TextField()
