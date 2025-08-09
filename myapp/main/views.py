from django.shortcuts import render


def index(request):
    """
    Вывод таблицы с информацией о всех движениях денежных средств.
    """

    context = {
        "title": "ДДС - Главная",
        "to_cash_flow": "Перейти к ДДС",
        'to_selectable_params': 'Перейти к парамметрам ДДС'
    }

    return render(request, "main/index.html", context)
