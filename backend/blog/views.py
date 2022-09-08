from django.shortcuts import render
from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializer


class List(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class DetailBlog(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer