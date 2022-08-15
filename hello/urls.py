from nturl2path import url2pathname
from django.urls import URLPattern, path
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
]