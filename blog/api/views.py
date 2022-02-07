from django.shortcuts import get_object_or_404

from blog.models import (
    BlogCategory,
    BlogSubCategory,
    Blog,
    BlogVideo
)
from blog.api.serializers import (
    BlogCategorySerializer,
    BlogSubCategorySerializer,
    BlogSerializer,
    BlogVideoSerializer
)

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def blog_api(request):
    try:
        queryset = Blog.objects.all()
        serializers = BlogSerializer(queryset, many=True)
        return Response(serializers.data)
    except Blog.DoesNotExist:
        return Response({"There is no Blog exits in database"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def blog_category_api(request, slug):
    """
    http://127.0.0.1:8000/api/category/python/
    :param request:
    :param slug:
    :return:
    """
    try:
        category_id = get_object_or_404(BlogCategory, slug=slug)
        queryset = Blog.objects.filter(category=category_id)
        serializers = BlogSerializer(queryset, many=True)
        return Response(serializers.data)
    except Blog.DoesNotExist:
        return Response({"There is no Blog  exits in database"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def blog_sub_category_api(request, cat_slug, sub_cat_slug):
    """
    http://127.0.0.1:8000/api/sub-category/python/django/
    :param request:
    :param cat_slug:
    :param sub_cat_slug:
    :return:
    """
    try:
        category_id = get_object_or_404(BlogCategory, slug=cat_slug)
        sub_category_id = get_object_or_404(BlogSubCategory, slug=sub_cat_slug)
        queryset = Blog.objects.filter(category=category_id, sub_category=sub_category_id)
        serializers = BlogSubCategorySerializer(queryset, many=True)
        return Response(serializers.data)
    except BlogSubCategory.DoesNotExist:
        return Response({"There is no BlogSubCategory exits in database"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def blog_video_api(request):
    try:
        queryset = BlogVideo.objects.all()
        serializers = BlogVideoSerializer(queryset, many=True)
        return Response(serializers.data)
    except BlogVideo.DoesNotExist:
        return Response({"There is no Blog Video exits in database"}, status=status.HTTP_404_NOT_FOUND)