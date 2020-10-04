from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=150)
    category = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to="%Y/%M/%d/")
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[Thumbnail(200, 300)],
        format='JPEG',
        options={'quality': 90}
    )
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='like_articles',
        blank=True)

    def __str__(self):
        return f'[id = {self.id}, title = {self.title}, content = {self.content}, created_at = {self.created_at}, updated_at = {self.updated_at}]'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'[pk={self.pk}, article = {self.article.title}, content = {self.content}, created_at = {self.created_at}]'