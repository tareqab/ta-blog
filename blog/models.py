from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    status_choices = (('P', 'published'),('D', 'draft'))

    title = models.CharField(max_length = 255)
    slug = models.CharField(max_length = 255, unique_for_date = 'publish')#publish date
    author = models.ForeignKey(User, related_name = 'blog_posts', on_delete = 'CASCADE')
    body = models.TextField()
    publish = models.DateTimeField(default = timezone.now)#publish date
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    status = models.CharField(max_length = 10, choices = status_choices, default = 'D')

    class Meta:
        ordering = ('-publish', )

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete = 'CASCADE')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ('created',)
    
    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)