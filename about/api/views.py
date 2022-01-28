from about.models import AboutMe
from about.api.serializers import AboutMeSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def about_me_api(request):
    try:
        queryset = AboutMe.objects.all()
        serializers = AboutMeSerializer(queryset, many=True)
        return Response(serializers.data)
    except AboutMe.DoesNotExist:
        return Response({"There is no slider exits in database"}, status=status.HTTP_404_NOT_FOUND)


