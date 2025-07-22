from django.urls import path
from .views import Home, Dashboard

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('dashboard/', Dashboard.as_view(), name='dash'),
]