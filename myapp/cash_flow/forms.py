from django import forms

from cash_flow.models import Cash_flow


class CashFlowForm(forms.ModelForm):
    """
    Форма для выполнения изменения записи о ДДС.

    Атрибуты:
        date_creation (date): дата создания записи о движении, заполняется автоматически значением текущей даты в формате дд.мм.гггг.
        status_id (int): внешний ключ ссылающийся на таблицу statuses.
        type_operation_id (int): внешний ключ, ссылающийся на таблицу types_operations.
        category_id (int): внешний ключ, ссылающийся на таблицу categories.
        subcategory_id (int): внешний ключ, ссылающийся на таблицу subcategories.
        amount (int): размер денежных средств (сумма) с которыми было выполнено движение.
        comment (str): комментарий свободной формы к выполненному движению.
    """

    class Meta:
        model = Cash_flow
        fields = "__all__"
        help_text = {
            "date_creation": "Дата выполнения",
            "status_id": "Статус",
            "type_operation_id": "Тип",
            "category_id": "Категория",
            "subcategory_id": "Подкатегория",
            "emount": "Сумма",
            "comment": "Комментарий",
        }
