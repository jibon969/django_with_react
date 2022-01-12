from rest_framework import status
from rest_framework.decorators import api_view
from home.models import Slider
from home.api.serializers import SliderSerializers
from rest_framework.response import Response


@api_view(['GET'])
def slider_list_api(request):
    try:
        slider = Slider.objects.filter(active=True).order_by('value')[:3]
        serializers = SliderSerializers(slider, many=True)
        return Response(serializers.data)
    except Slider.DoesNotExist:
        return Response({"There is no slider exits in database"}, status=status.HTTP_404_NOT_FOUND)
