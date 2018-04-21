from django.db import models

from user.models import UserProfile


class Category(models.Model):
    name = models.CharField(max_length=50, blank=False)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return str(self.name)


class Article(models.Model):
    title = models.CharField(max_length=100, blank=False, default='')
    cate = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING)
    content = models.TextField(max_length=5000, blank=False, null=False)
    thumbnail = models.ImageField(null=True, blank=True, default=None, upload_to='thumb')
    ip_address = models.GenericIPAddressField(unpack_ipv4=True, blank=True, null=True)
    is_top = models.BooleanField('置顶', default=False)
    allow_comments = models.BooleanField('允许评论', default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_top', '-updated']

    def __str__(self):
        return str(self.title)