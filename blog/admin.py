from django.contrib import admin
from .models import BlogCategory, BlogSubCategory, Blog, BlogVideo, Advertisement, Comment
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class BlogCategoryResource(resources.ModelResource):
    class Meta:
        model = BlogCategory
        fields = ('id', 'title', 'slug')


class BlogCategoryAdmin(ImportExportModelAdmin):
    resource_class = BlogCategoryResource
    list_display = ['title', 'slug', 'timestamp']
    search_fields = ['title']
    list_filter = ['title']
    list_per_page = 20


admin.site.register(BlogCategory, BlogCategoryAdmin)


# Customized SubCategory models or table CSV File
class BlogSubCategoryResource(resources.ModelResource):
    class Meta:
        model = BlogSubCategory
        fields = ('id', 'title', 'slug')


class SubCategoryAdmin(ImportExportModelAdmin):
    resource_class = BlogSubCategoryResource
    list_display = ['title', 'slug', 'timestamp']
    search_fields = ['title']
    list_filter = ['title']
    list_per_page = 20


admin.site.register(BlogSubCategory, SubCategoryAdmin)


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'timestamp']
    list_per_page = 20
    search_fields = ['title']

    class Meta:
        model: Blog


admin.site.register(Blog, BlogAdmin)


class BlogVideoAdmin(admin.ModelAdmin):
    list_display = ['title',  'video', 'timestamp']
    list_per_page = 20
    search_fields = ['title']

    class Meta:
        model: BlogVideo


admin.site.register(BlogVideo, BlogVideoAdmin)


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['title', 'url_field', 'timestamp']
    list_per_page = 20
    search_fields = ['title']

    class Meta:
        model = Advertisement


admin.site.register(Advertisement, AdvertisementAdmin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approve')
    list_filter = ('approve', 'created_on')
    search_fields = ('name', 'email', 'body')
    list_editable = ['approve']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approve=True)