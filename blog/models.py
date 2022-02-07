from ckeditor.fields import RichTextField
from django.db import models
from django.db.models.signals import pre_save
from .utils import blog_unique_slug_generator
from embed_video.fields import EmbedVideoField


class BlogCategory(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(null=True, blank=True, max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']


def blog_category_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = blog_unique_slug_generator(instance)


pre_save.connect(blog_category_pre_save_receiver, sender=BlogCategory)


class BlogSubCategory(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(null=True, blank=True, max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']


def blog_sub_category_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = blog_unique_slug_generator(instance)


pre_save.connect(blog_sub_category_pre_save_receiver, sender=BlogSubCategory)


class Blog(models.Model):
    blog_title = models.CharField(max_length=250, blank=True, null=True)
    title = models.CharField(max_length=120, help_text="This title generate unique url Slug, title must be english")
    focus_keyword = models.TextField(blank=True, null=True)
    meta_description = models.TextField(max_length=160, blank=True, null=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(BlogSubCategory, on_delete=models.CASCADE, blank=True, null=True)
    image = models.FileField(upload_to="blog/")
    facebook_url = models.URLField(blank=True, null=True, max_length=50)
    instagram_url = models.URLField(blank=True, null=True, max_length=50)
    twitter_url = models.URLField(blank=True, null=True, max_length=50)
    linkedin_url = models.URLField(blank=True, null=True, max_length=50)
    description = RichTextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True, max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']


def blog_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = blog_unique_slug_generator(instance)


pre_save.connect(blog_pre_save_receiver, sender=Blog)


class BlogVideo(models.Model):
    title = models.CharField(max_length=120)
    video = EmbedVideoField()  # same like models.URLField()
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']


class Advertisement(models.Model):
    title = models.CharField(max_length=120, blank=True, null=True)
    image = models.FileField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    url_field = models.URLField(max_length=120, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']


class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField(blank=True, null=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approve = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
