from typing import Any
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from selectable_params.models import (
    Categories,
    Statuses,
    Subcategories,
    Types_operations,
)
from selectable_params.forms import StatusForm, TypeForm, CategoryForm, SubcategoryForm


def get_selectable_params(request) -> HttpResponse:
    """
    Вывод таблиц с информацией о всех статусах, типах, категориях и подкатегориях
    движениях денежных средств с указанной фильтрацией.
    """

    # Данные
    all_statuses = Statuses.objects.all().order_by("name")
    all_types = Types_operations.objects.all().order_by("name")
    all_categories = Categories.objects.all().order_by("name")
    all_subcategories = Subcategories.objects.all().order_by("category_id")

    # Проверка данных
    if not all(
        [
            all_statuses.exists(),
            all_types.exists(),
            all_categories.exists(),
            all_subcategories.exists(),
        ]
    ):
        raise Http404()

    context: dict[str, Any] = {
        "title": "Парамметры ДДС",
        "all_statuses": all_statuses,
        "all_types": all_types,
        "all_categories": all_categories,
        "all_subcategories": all_subcategories,
    }

    return render(request, "selectable_params/selectable_params.html", context)


def create_status(request):
    """
    Контроллер создания нового статуса ДДС.
    """

    template = "selectable_params/create_status.html"

    if request.method == "POST":
        form = StatusForm(request.POST or None)

        if form.is_valid():
            new_status = Statuses(
                name=form.cleaned_data["name"],
            )
            new_status.save()

    form = StatusForm()

    context: dict[str, Any] = {
        "title": "Создание нового статуса ДДС",
        "form": form,
    }

    return render(request, template, context)


def create_type(request):
    """
    Контроллер создания нового типа ДДС.
    """

    template = "selectable_params/create_type.html"

    if request.method == "POST":
        form = TypeForm(request.POST or None)

        if form.is_valid():
            new_type = Types_operations(
                name=form.cleaned_data["name"],
            )
            new_type.save()

    form = TypeForm()

    context: dict[str, Any] = {
        "title": "Создание нового типа ДДС",
        "form": form,
    }

    return render(request, template, context)


def create_category(request):
    """
    Контроллер создания нового типа ДДС.
    """

    template = "selectable_params/create_category.html"

    if request.method == "POST":
        form = CategoryForm(request.POST or None)

        if form.is_valid():
            new_category = Categories(
                name=form.cleaned_data["name"],
                type_operation=form.cleaned_data["type_operation"],
            )
            new_category.save()

    form = CategoryForm()

    context: dict[str, Any] = {
        "title": "Создание нового типа ДДС",
        "form": form,
    }

    return render(request, template, context)


def create_subcategory(request):
    """
    Контроллер создания нового типа ДДС.
    """

    template = "selectable_params/create_subcategory.html"

    if request.method == "POST":
        form = SubcategoryForm(request.POST or None)

        if form.is_valid():
            new_subcategory = Subcategories(
                name=form.cleaned_data["name"],
                category=form.cleaned_data["category"],
            )
            new_subcategory.save()

    form = SubcategoryForm()

    context: dict[str, Any] = {
        "title": "Создание нового типа ДДС",
        "form": form,
    }

    return render(request, template, context)


def change_status(request, pk: int):
    """
    Контроллер изменения существующего статуса ДДС.
    """

    template = "selectable_params/change_status.html"

    cur_status = get_object_or_404(Statuses, id=pk)

    if request.method == "POST":
        form = StatusForm(request.POST or None)

        if form.is_valid():
            cur_status.name = form.cleaned_data["name"]
            cur_status.save()
            return redirect("selectable_params:change_status", pk=cur_status.id)

    cur_status_data: dict[str, Any] = {
        "name": cur_status.name,
    }

    form = StatusForm(cur_status_data)

    context: dict[str, Any] = {
        "title": "Изменение статуса ДДС",
        "form": form,
        "cur_status": cur_status,
    }
    return render(request, template, context)


def delete_status(request, pk: int):
    """
    Удаляет статус ДДС.
    """

    context: dict[str, Any] = {
        "title": "Удаление статуса ДДС",
        "message": "запись не найдена.",
    }

    cur_status: Statuses = Statuses.objects.get(id=pk)

    if cur_status:
        cur_status.delete()
        context["message"] = "успешно."

    return render(request, "selectable_params/delete.html", context)


def change_type(request, pk: int):
    """
    Контроллер изменения существующего типа ДДС.
    """

    template = "selectable_params/change_type.html"

    cur_type: Types_operations = get_object_or_404(Types_operations, id=pk)

    if request.method == "POST":
        form = TypeForm(request.POST or None)

        if form.is_valid():
            cur_type.name = form.cleaned_data["name"]
            cur_type.save()
            return redirect("selectable_params:change_type", pk=cur_type.id)

    cur_type_data: dict[str, Any] = {
        "name": cur_type.name,
    }

    form = TypeForm(cur_type_data)

    context: dict[str, Any] = {
        "title": "Изменение типа ДДС",
        "form": form,
        "cur_type": cur_type,
    }
    return render(request, template, context)


def delete_type(request, pk: int):
    """
    Удаляет тип ДДС.
    """

    context: dict[str, Any] = {
        "title": "Удаление типа ДДС",
        "message": "запись не найдена.",
    }

    cur_type: Types_operations = Types_operations.objects.get(id=pk)

    if cur_type:
        cur_type.delete()
        context["message"] = "успешно."

    return render(request, "selectable_params/delete.html", context)


def change_category(request, pk: int):
    """
    Контроллер изменения существующей категории ДДС.
    """

    template = "selectable_params/change_category.html"

    cur_category: Categories = get_object_or_404(Categories, id=pk)
    cur_type = get_object_or_404(Types_operations, id=cur_category.type_operation_id)

    if request.method == "POST":
        form = CategoryForm(request.POST or None)

        if form.is_valid():
            cur_category.name = form.cleaned_data["name"]
            cur_category.save()
            return redirect("selectable_params:change_category", pk=cur_category.id)

    cur_category_data: dict[str, Any] = {
        "name": cur_category.name,
        'type_operation': cur_type.id
    }

    form = CategoryForm(cur_category_data)

    context: dict[str, Any] = {
        "title": "Изменение категории ДДС",
        "form": form,
        "cur_category": cur_category,
    }
    return render(request, template, context)


def delete_category(request, pk: int):
    """
    Удаляет категорию ДДС.
    """

    context: dict[str, Any] = {
        "title": "Удаление категории ДДС",
        "message": "запись не найдена.",
    }

    cur_category: Categories = Categories.objects.get(id=pk)

    if cur_category:
        cur_category.delete()
        context["message"] = "успешно."

    return render(request, "selectable_params/delete.html", context)


def change_subcategory(request, pk: int):
    """
    Контроллер изменения существующей подкатегории ДДС.
    """

    template = "selectable_params/change_subcategory.html"

    cur_subcategory: Subcategories = get_object_or_404(Subcategories, id=pk)

    if request.method == "POST":
        form = SubcategoryForm(request.POST or None)

        if form.is_valid():
            cur_subcategory.name = form.cleaned_data["name"]
            cur_subcategory.category = form.cleaned_data["category"]
            cur_subcategory.save()
            return redirect(
                "selectable_params:change_subcategory", pk=cur_subcategory.id
            )

    cur_subcategory_data: dict[str, Any] = {
        "name": cur_subcategory.name,
        "category": cur_subcategory.category,
    }

    form = SubcategoryForm(cur_subcategory_data)

    context: dict[str, Any] = {
        "title": "Изменение подкатегории ДДС",
        "form": form,
        "cur_subcategory": cur_subcategory,
    }
    return render(request, template, context)


def delete_subcategory(request, pk: int):
    """
    Удаляет подкатегорию ДДС.
    """

    context: dict[str, Any] = {
        "title": "Удаление статуса ДДС",
        "message": "запись не найдена.",
    }

    cur_subcategory: Subcategories = Subcategories.objects.get(id=pk)

    if cur_subcategory:
        cur_subcategory.delete()
        context["message"] = "успешно."

    return render(request, "selectable_params/delete.html", context)
