from django.urls import path, include
from . import views


urlpatterns = [

    # api urls/endpoint
    path('api/', include('blog.api.urls')),

    path('blog/', views.blog_view, name="blog"),
    path('blog/category/<slug:slug>/', views.blog_category, name="category"),
    path('blog/<slug:cat_slug>/<slug:sub_cat_slug>/', views.blog_sub_category, name='category-and-subcategory'),
    path('blog-detail/<slug:slug>/', views.blog_detail, name="blog-detail"),

    # Blog urls list
    path('blog-list/', views.blog_list, name="blog-list"),
    path('add-blog/', views.add_blog, name="add-blog"),
    path('update-blog/<int:id>/', views.update_blog, name="update-blog"),
    path('delete-blog/<int:id>/', views.delete_blog, name="delete-blog"),

    # Comment Urls
    path('blog-comment/', views.blog_comment, name="blog-comment"),
    path('update-comment/<int:id>/', views.update_comment, name="update-comment"),
    path('delete-comment/<int:id>/', views.delete_comment, name='delete-comment'),

    # Category url list
    path('blog-category-list/', views.blog_category_list, name="blog-category-list"),
    path('blog-category-form/', views.blog_category_form, name="blog-category-form"),
    path('blog-update-category/<int:id>/', views.blog_update_category, name="blog-update-category"),
    path('blog-delete-category/<int:id>/', views.blog_delete_category, name="blog-delete-category"),
    path('blog-download-category-csv/', views.blog_download_category_csv, name="blog-download-category-csv"),

    # Sub Category url list
    path('blog-sub-category-list/', views.blog_sub_category_list, name="blog-sub-category-list"),
    path('blog-sub-category-form/', views.blog_sub_category_form, name="blog-sub-category-form"),
    path('blog-update-sub-category/<int:id>/', views.blog_sub_update_category, name="blog-update-sub-category"),
    path('blog-delete-sub-category/<int:id>/', views.blog_sub_delete_category, name="blog-delete-sub-category"),
    path('blog-download-sub-category-csv/', views.blog_sub_download_category_csv, name="blog-download-sub-category-csv"),


]