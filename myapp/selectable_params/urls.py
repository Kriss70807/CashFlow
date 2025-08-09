from django.urls import URLPattern, path

from selectable_params import views


app_name = "selectable_params"

urlpatterns: list[URLPattern] = [
    path("", views.get_selectable_params, name="selectable_params"),
    path("create_status", views.create_status, name="create_status"),
    path("create_type", views.create_type, name="create_type"),
    path("create_category", views.create_category, name="create_category"),
    path("create_subcategory", views.create_subcategory, name="create_subcategory"),
    path("change_status/<int:pk>", views.change_status, name="change_status"),
    path("delete_status/<int:pk>", views.delete_status, name="delete_status"),
    path("change_type/<int:pk>", views.change_type, name="change_type"),
    path("delete_type/<int:pk>", views.delete_type, name="delete_type"),
    path("change_category/<int:pk>", views.change_category, name="change_category"),
    path("delete_category/<int:pk>", views.delete_category, name="delete_category"),
    path("change_subcategory/<int:pk>", views.change_subcategory, name="change_subcategory"),
    path("delete_subcategory/<int:pk>", views.delete_subcategory, name="delete_subcategory"),
]
