from typing import Literal

from django.db import models


class Statuses(models.Model):
    """
    Класс, представляющий собой данные о статусах движений денежных средств в таблице statuses.

    Атрибут:
        name: хранит название статуса в качестве значения.
    """

    name = models.CharField(max_length=100, verbose_name="Статус")

    class Meta:
        db_table: str = "statuses"
        verbose_name: str = "Статус"
        verbose_name_plural: str = "Статусы"
        ordering: tuple[Literal["name"]] = ("name",)
    
    def __str__(self) -> str:
        return self.name


class Types_operations(models.Model):
    """
    Класс, представляющий собой данные о типах движений денежных средств в таблице types_operations.

    Атрибут:
        name: хранит название типа в качестве значения.
    """

    name = models.CharField(max_length=100, verbose_name="Тип")

    class Meta:
        db_table: str = "types_operations"
        verbose_name: str = "Тип"
        verbose_name_plural: str = "Типы"
        ordering: tuple[Literal["name"]] = ("name",)
    
    def __str__(self) -> str:
        return self.name


class Categories(models.Model):
    """
    Класс, представляющий собой данные о категориях движений денежных средств в таблице categories.

    Атрибут:
        name: хранит название категории в качестве значения.
    """

    name = models.CharField(max_length=100, verbose_name="Категория")
    type_operation = models.ForeignKey(
        to=Types_operations, on_delete=models.CASCADE, verbose_name="Тип", editable=True
    )

    class Meta:
        db_table: str = "categories"
        verbose_name: str = "Категория"
        verbose_name_plural: str = "Категории"
        ordering: tuple[Literal["name"]] = ("name",)
    
    def __str__(self) -> str:
        return self.name


class Subcategories(models.Model):
    """
    Класс, представляющий собой данные о подкатегориях движений денежных средств в таблице subcategories.

    Атрибут:
        name: хранит название подкатегории в качестве значения.
        category: является внешним ключом, ссылающим на таблицу categories.
    """

    name = models.CharField(max_length=100, verbose_name="Подкатегория")
    category = models.ForeignKey(
        to=Categories, on_delete=models.CASCADE, verbose_name="Категория", editable=True
    )

    class Meta:
        db_table: str = "subcategories"
        verbose_name: str = "Подкатегория"
        verbose_name_plural: str = "Подкатегории"
        ordering: tuple[Literal["name"]] = ("name",)
    
    def __str__(self) -> str:
        return self.name
