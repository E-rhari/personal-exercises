from django.urls import  path
from . import views


urlpatterns = [
    path("chirashizushi/", views.chirashizushi, name='chirashizushi'),
    path("tsurasuzusu/",   views.tsurasuzusu,   name="tsurasuzusu")
]