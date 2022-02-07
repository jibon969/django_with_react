from rest_framework import serializers
from blog.models import (
    BlogCategory,
    BlogSubCategory,
    Blog,
    BlogVideo
)


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = '__all__'


class BlogSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogSubCategory
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class BlogVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogVideo
        fields = '__all__'

