
from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    blog_title = models.CharField(max_length = 800, blank = True, null = True)
    blog_body = models.CharField(max_length = 5000, blank = True, null = True)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    updated = models.DateTimeField(auto_now = True, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        #return self.blog_title, self.blog_body
        return f'{self.blog_title} {self.blog_body}'