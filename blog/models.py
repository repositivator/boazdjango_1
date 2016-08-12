from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.user')
    title = models.CharField(max_length=200)
    text = models.TextField(null=False)
    
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null=True)
    
    def __str__(self):
        return self.title
        
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.ForeignKey('auth.user')
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    
    def __str__(self):
        return self.text