from django.urls import path
from . import views, new


urlpatterns = [
    path('', views.index),
    path('new/', new.index),
]