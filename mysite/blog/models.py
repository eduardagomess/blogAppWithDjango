from django.conf import settings
from django.db import models
from django.utils import timezone

# models.Model significa que o Post é um modelo de Django, logo deve ser salvo no banco de dados
class Post(models.Model):
    # link para outro modelo
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #texto com um número limitado de caracteres
    title = models.CharField(max_length=200)
    #campo é para textos sem um limite fixo
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
