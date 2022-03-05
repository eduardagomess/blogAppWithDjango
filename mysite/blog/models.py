from django.conf import settings
from django.db import models
from django.utils import timezone

# models.Model means the Post is a Django model, so it must be saved in the database
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #text with a limited number of characters
    title = models.CharField(max_length=200)
    #text without a fixed limit of characters
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
