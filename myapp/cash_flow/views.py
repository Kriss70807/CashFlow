from datetime import date, timedelta
from typing import Any
from unicodedata import category
from django.db.models import QuerySet
from django.http import Http404, HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render

from cash_flow.forms import CashFlowForm
from cash_flow.models import Cash_flow
from selectable_params.models import (
    Statuses,
    Types_operations,
    Categories,
    Subcategories,
)


def get_cash_flow(request, filter_slug: str = "all_date") -> HttpResponse:
    """
    Вывод таблицы с информацией о всех движениях денежных средств с указанной фильтрацией.
    """

    # Параметры фильтрации
    on_date = request.GET.get("on_date", "all_date")
    on_status = request.GET.get("on_status", None)
    on_type = request.GET.get("on_type", None)
    on_category = request.GET.get("on_category", None)
    on_subcategory = request.GET.get("on_subcategory", None)

    # Данные
    all_cash_flow = Cash_flow.objects.all()
    all_statuses = Statuses.objects.all()
    all_types = Types_operations.objects.all()
    all_categories = Categories.objects.all()
    all_subcategories = Subcategories.objects.all()

    # Проверка данных
    if not all(
        [
            all_cash_flow.exists(),
            all_statuses.exists(),
            all_types.exists(),
            all_categories.exists(),
            all_subcategories.exists(),
        ]
    ):
        raise Http404()

    # Фильтрация по дате
    if on_date:
        filter_slug = on_date
        if on_date == "today":
            now = date.today()
            all_cash_flow = all_cash_flow.filter(date_creation=now)

        elif on_date == "last_week":
            week_ago = date.today() - timedelta(weeks=1)
            all_cash_flow = all_cash_flow.filter(date_creation__gte=week_ago).order_by(
                "-date_creation"
            )

        elif on_date == "last_week":
            month_ago = date.today() - timedelta(weeks=4.3481)
            all_cash_flow = all_cash_flow.filter(date_creation__gte=month_ago).order_by(
                "-date_creation"
            )

        else:
            all_cash_flow = all_cash_flow.order_by("-date_creation")

    # Фильтрация по статусу
    if on_status:
        filter_slug = on_status
        all_cash_flow = all_cash_flow.filter(status=on_status)

    # Фильтрация по типу
    if on_type:
        filter_slug = on_type
        all_cash_flow = all_cash_flow.filter(type_operation=on_type)

    # Фильтрация по категории
    if on_category:
        filter_slug = on_category
        all_cash_flow = all_cash_flow.filter(category=on_category)

    # Фильтрация по подкатегории
    if on_subcategory:
        filter_slug = on_subcategory
        all_cash_flow = all_cash_flow.filter(subcategory=on_subcategory)

    context: dict[str, Any] = {
        "title": "Кошельки",
        "all_cash_flow": all_cash_flow,
        "all_statuses": all_statuses,
        "all_types": all_types,
        "all_categories": all_categories,
        "all_subcategories": all_subcategories,
        "filter_slug": filter_slug,
    }

    return render(request, "cash_flow/cash_flow.html", context)


def delete_cash_flow(request, pk: int):
    """
    Удаляет запись о ДДС по её ключу.
    """

    context: dict[str, Any] = {
        "title": "Удаление записи о ДДС",
        "message": "запись не найдена.",
    }

    cash_flow = Cash_flow.objects.get(id=pk)

    if cash_flow:
        cash_flow.delete()
        context["message"] = "успешно."

    return render(request, "cash_flow/delete.html", context)


def change_cash_flow(request, pk: int):
    """
    Контроллер изменения существующей записи о конкретном ДДС.
    """

    template = "cash_flow/change.html"

    cur_cash_flow = get_object_or_404(Cash_flow, id=pk)


    if request.method == "POST":
        form = CashFlowForm(request.POST or None)

        if form.is_valid():
            cur_cash_flow.date_creation = form.cleaned_data['date_creation']
            cur_cash_flow.status_id = form.cleaned_data['status']
            cur_cash_flow.type_operation_id = form.cleaned_data['type_operation']
            cur_cash_flow.category_id = form.cleaned_data['category']
            cur_cash_flow.subcategory_id = form.cleaned_data['subcategory']
            cur_cash_flow.amount = form.cleaned_data['amount']
            cur_cash_flow.comment = form.cleaned_data['comment']
            cur_cash_flow.save()
            return redirect("cash_flow:change_cash_flow", pk=cur_cash_flow.id)

    cur_cash_flow_data: dict[str, Any] = {
        "date_creation": cur_cash_flow.date_creation,
        "status": cur_cash_flow.status,
        "type_operation": cur_cash_flow.type_operation,
        "category": cur_cash_flow.category,
        "subcategory": cur_cash_flow.subcategory,
        "amount": cur_cash_flow.amount,
        "comment": cur_cash_flow.comment,
    }

    form = CashFlowForm(cur_cash_flow_data)

    context: dict[str, Any] = {
        "title": "Изменение ДДС",
        "form": form,
        "cur_cash_flow": cur_cash_flow,
    }
    return render(request, template, context)


def create_cash_flow(request):
    """
    Контроллер создания записи о новом ДДС.
    """

    template = "cash_flow/create.html"

    if request.method == "POST":
        form = CashFlowForm(request.POST or None)

        if form.is_valid():
            new_cash_flow = Cash_flow(
                date_creation=form.cleaned_data["date_creation"],
                status=form.cleaned_data["status"],
                type_operation=form.cleaned_data["type_operation"],
                category=form.cleaned_data["category"],
                subcategory=form.cleaned_data["subcategory"],
                amount=form.cleaned_data["amount"],
                comment=form.cleaned_data["comment"],
            )
            new_cash_flow.save()

    
    form = CashFlowForm()

    context: dict[str, Any] = {
        "title": "Создание новой записи ДДС",
        "form": form,
    }

    return render(request, template, context)
