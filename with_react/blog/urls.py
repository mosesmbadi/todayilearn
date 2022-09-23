from django.urls import path

from . import views

urlpatterns = [
    path('', views.List.as_view()),
    path('<int:pk>/', views.DetailBlog.as_view()),
    #added below for texting ckeditor
    # path('add_post/', views.AddPostView.as_view(), name='add_post'),
    # path('all_post/', views.SeePostView.as_view(), name='see_post'),
]