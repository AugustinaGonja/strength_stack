from django.urls import path
from .views import Home, Dashboard , About

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('dashboard/', Dashboard.as_view(), name='dash'),
    path('about/', About.as_view(), name='about'),
]