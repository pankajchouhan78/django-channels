from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    like = models.ManyToManyField(User, related_name="sandwiches", blank=True)

    def __str__(self):
        return self.title