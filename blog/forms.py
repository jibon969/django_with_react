from django import forms
from django.forms import Textarea
from .models import Blog, Advertisement, Comment, BlogCategory, BlogSubCategory


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            'blog_title',
            'title',
            'category',
            'sub_category',
            'image',
            'facebook_url',
            'instagram_url',
            'twitter_url',
            'linkedin_url',
            'description',
        ]


class CreateAdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = [
            'title',
            'image',
            'url_field'
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body', 'approve']

        # Override the Customer some fields
        widgets = {
            'body': Textarea(attrs={'rows': 3, 'cols': 3}),
        }


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = BlogCategory
        fields = [
            'title',
        ]


class SubCategoryCreateForm(forms.ModelForm):
    class Meta:
        model = BlogSubCategory
        fields = [
            'title',
        ]