from django.urls import path
from about.api import views

urlpatterns = [
    path('about-me', views.about_me_api, name="about-me")
]