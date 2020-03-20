from django.db import models
from django.conf import settings
from django.utils import timezone
import markdown2


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    thumbnail_link = models.URLField(max_length=500)

    def reading_duration(self):
        return len(self.text) // 1500 + 1

    def html_text(self):
        return markdown2.markdown(self.text, extras=["fenced code blocks"])

    def __str__(self):
        return self.title
