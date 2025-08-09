from django.urls import URLPattern, path

from main.views import index

app_name = "main"

urlpatterns: list[URLPattern] = [
    path("", index, name="index"),
]
