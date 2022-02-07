from rest_framework import serializers
from home.models import Slider, Post, Category


class SliderSerializers(serializers.ModelSerializer):
    extra_large_url = serializers.SerializerMethodField("get_extra_large_device_image")
    large_device_url = serializers.SerializerMethodField("get_large_device_url_image")
    medium_device_url = serializers.SerializerMethodField("get_medium_device_url_image")
    small_device_url = serializers.SerializerMethodField("get_small_devices_url_image")

    class Meta:
        model = Slider
        fields = [
            'title',
            'extra_large_url',
            'large_device_url',
            'medium_device_url',
            'small_device_url',
            'url_field',
            'value',
            'active',
        ]

    # This method return slider image url
    def get_extra_large_device_image(self, model):
        return "http://127.0.0.1:8000" + model.extraLargeDevices.url

    def get_large_device_url_image(self, model):
        return "http://127.0.0.1:8000" + model.largeDevices.url

    def get_medium_device_url_image(self, model):
        return "http://127.0.0.1:8000" + model.mediumDevices.url

    def get_small_devices_url_image(self, model):
        return "http://127.0.0.1:8000" + model.smallDevices.url


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')


class PostSerializers(serializers.ModelSerializer):
    image = serializers.SerializerMethodField("get_image_url")
    category = serializers.CharField(source='category.title')

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'category',
            'description',
            'short_description',
            'image',
            'slug',
        ]

    def get_image_url(self, model):
        return "http://127.0.0.1:8000" + model.image.url




