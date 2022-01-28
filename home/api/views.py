from rest_framework import status
from rest_framework.decorators import api_view
from home.models import Slider, Post
from home.api.serializers import SliderSerializers, PostSerializers
from rest_framework.response import Response


@api_view(['GET'])
def slider_list_api(request):
    try:
        slider = Slider.objects.filter(active=True).order_by('value')[:3]
        serializers = SliderSerializers(slider, many=True)
        return Response(serializers.data)
    except Slider.DoesNotExist:
        return Response({"There is no slider exits in database"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def post_list(request):
    try:
        post = Post.objects.all()
        serializers = PostSerializers(post, many=True)
        return Response(serializers.data)
    except Post.DoesNotExist:
        return Response({"There is no Post exits in database"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def post_details(request, slug):
    try:
        post = Post.objects.get(slug__icontains=slug)
        serializers = PostSerializers(post)
        return Response(serializers.data)
    except Post.DoesNotExist:
        return Response({"There is no Post exits in database"}, status=status.HTTP_404_NOT_FOUND)