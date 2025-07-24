from django.urls import path
from .views import Home, Dashboard , About, Register

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('dashboard/', Dashboard.as_view(), name='dash'),
    path('about/', About.as_view(), name='about'),
    path('registration/', Register.as_view(), name='register'),
]