from django.db import models
from ckeditor.fields import RichTextField

class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    #testing ckeditor
    content = RichTextField(blank=True,null=True)

    def __str__(self):
        return self.title


# class User(models.Model):
#     user_name = models.CharField(max_length=70)
#     pwd = models.CharField(max_length=100)

#     def __str__(self):
#         return self.user_name



# class Post(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     content = RichTextField(blank=True,null=True)

#     def __str__(self):
#         return self.title