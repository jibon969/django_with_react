from django.urls import path
from blog.api import views

urlpatterns = [
    path('blog-category/', views.blog_category_api, name="blog-category"),
    path('blog-sub-category/', views.blog_sub_category_api, name="blog-sub-category"),
    path('blog/', views.blog_api, name="blog"),
    path('blog-video/', views.blog_video_api, name="blog-video"),
]