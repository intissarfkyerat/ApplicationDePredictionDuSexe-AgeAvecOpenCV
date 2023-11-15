
from django.urls import path
from system.views import Home
urlpatterns = [
    path('', Home, name="home"),
]