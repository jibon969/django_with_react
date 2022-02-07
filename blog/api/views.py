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
def blog_category_api(request):
    try:
        queryset = BlogCategory.objects.all()
        serializers = BlogCategorySerializer(queryset, many=True)
        return Response(serializers.data)
    except BlogCategory.DoesNotExist:
        return Response({"There is no Blog Category exits in database"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def blog_sub_category_api(request):
    try:
        queryset = BlogSubCategory.objects.all()
        serializers = BlogSubCategorySerializer(queryset, many=True)
        return Response(serializers.data)
    except BlogSubCategory.DoesNotExist:
        return Response({"There is no BlogSubCategory exits in database"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def blog_api(request):
    try:
        queryset = Blog.objects.all()
        serializers = BlogSerializer(queryset, many=True)
        return Response(serializers.data)
    except Blog.DoesNotExist:
        return Response({"There is no Blog exits in database"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def blog_video_api(request):
    try:
        queryset = BlogVideo.objects.all()
        serializers = BlogVideoSerializer(queryset, many=True)
        return Response(serializers.data)
    except BlogVideo.DoesNotExist:
        return Response({"There is no Blog Video exits in database"}, status=status.HTTP_404_NOT_FOUND)