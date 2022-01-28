from django.contrib import admin
from .models import AboutMe
# Register your models here.


class AboutMeAdmin(admin.ModelAdmin):
    list_display = ['name', 'position']
    search_fields = ['name', 'position']
    class Meta:
        model = AboutMe


admin.site.register(AboutMe, AboutMeAdmin)


