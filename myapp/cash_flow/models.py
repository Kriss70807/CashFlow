from datetime import date

from django.db import models

from selectable_params.models import (
    Statuses,
    Types_operations,
    Categories,
    Subcategories,
)


class Cash_flow(models.Model):
    """
    Класс, представляющий собой данные о движениях денежных средств (далее по тексту - движение) в таблице cash_flow.

    Атрибуты:
        date_creation (date): дата создания записи о движении, заполняется автоматически значением текущей даты в формате дд.мм.гггг.
        status_id (int): внешний ключ ссылающийся на таблицу statuses.
        type_operation_id (int): внешний ключ, ссылающийся на таблицу types_operations.
        category_id (int): внешний ключ, ссылающийся на таблицу categories.
        subcategory_id (int): внешний ключ, ссылающийся на таблицу subcategories.
        amount (int): размер денежных средств (сумма) с которыми было выполнено движение.
        comment (str): комментарий свободной формы к выполненному движению.
    """

    date_creation = models.DateField(
        default=date.today, verbose_name="Дата выполнения"
    )

    status = models.ForeignKey(
        to=Statuses, on_delete=models.PROTECT, verbose_name="Статус"
    )

    type_operation = models.ForeignKey(
        to=Types_operations, on_delete=models.PROTECT, verbose_name="Тип"
    )

    category = models.ForeignKey(
        to=Categories, on_delete=models.PROTECT, verbose_name="Категория",
    )

    subcategory = models.ForeignKey(
        to=Subcategories, on_delete=models.PROTECT, verbose_name="Подкатегория"
    )

    amount = models.IntegerField(null=False, verbose_name="Сумма")
    comment = models.TextField(max_length=300, null=True, verbose_name="Комментарий")

    class Meta:
        db_table = "cash_flow"
        verbose_name = "Движение денежных средств"
        verbose_name_plural = "Движения денежных средств"
        ordering = ("date_creation",)

    # def __str__(self):
    #     return f"{self.date_creation.strftime('%d.%m.%Y')}: {self.type_operation_id} {self.amount} р - {self.status_id} ({self.category_id}/{self.subcategory_id})"
