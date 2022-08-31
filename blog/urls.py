from django.contrib import admin
from django.urls import path, include
from blog import urls as blog_urls
from .views import (
      BlogListApiView,
      BlogDetailApiView
      )

urlpatterns = [
    path('api', BlogListApiView.as_view()),
    path('api/<int:blog_id>/', BlogDetailApiView.as_view()),
]
