from django.db import models
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField(blank=True, null=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(
            default=timezone.now)
