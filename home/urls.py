from django.urls import path, include

urlpatterns = [
    # api urls/endpoint
    path('api/', include('home.api.urls')),

]
