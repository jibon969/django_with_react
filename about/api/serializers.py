from rest_framework import serializers
from about.models import AboutMe


class AboutMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMe
        fields = '__all__'

