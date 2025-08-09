from django.urls import URLPattern, path

from cash_flow.views import (
    change_cash_flow,
    get_cash_flow,
    delete_cash_flow,
    create_cash_flow,
)

app_name = "cash_flow"

urlpatterns: list[URLPattern] = [
    path("create_cash_flow", create_cash_flow, name="create_cash_flow"),
    path("<str:filter_slug>", get_cash_flow, name="cash_flow"),
    path("delete_cash_flow/<int:pk>", delete_cash_flow, name="delete_cash_flow"),
    path("change_cash_flow/<int:pk>", change_cash_flow, name="change_cash_flow"),
]
