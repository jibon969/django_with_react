from django.urls import path
from blog.api import views

urlpatterns = [
    path('blog/', views.blog_api, name="blog"),
    path('category/<slug:slug>/', views.blog_category_api),
    path('sub-category/<slug:cat_slug>/<slug:sub_cat_slug>/', views.blog_sub_category_api),
    path('blog-video/', views.blog_video_api, name="blog-video"),
]