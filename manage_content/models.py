from django.db import models
from tinymce import models as tinymce_models
import re

# Create your models here.


class Page(models.Model):

    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title


class Post(models.Model):

    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = tinymce_models.HTMLField()
    ORDER_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
    ]
    order = models.SmallIntegerField(choices=ORDER_CHOICES, default=1)

    def __str__(self):
        return self.title

    def htmlid(self):
        htmlid = self.title.lower().replace(' ', '_')
        htmlid = re.sub('[^(a-z)(A-Z)(0-9)._-]', '', htmlid)
        return '{0}-{1}'.format(htmlid, self.id)

    class Meta:
        ordering = ['page', 'order']

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/{1}/{2}'.format(instance.post.page, instance.post, filename)


class PostGallery(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField(upload_to=user_directory_path, max_length=255)

    def __str__(self):
        return self.post.title

    class Meta:
        verbose_name = 'postgallery'
        verbose_name_plural = 'post gallery'
        ordering = ('post__title',)
