from django import forms

from selectable_params.models import Statuses, Types_operations, Categories, Subcategories

class StatusForm(forms.ModelForm):
    '''
    Форма для выполнения работы со статусами ДДС.
    '''

    class Meta:
        model = Statuses
        fields = '__all__'
        help_text = {
            'name': 'Название статуса',
        }


class TypeForm(forms.ModelForm):
    '''
    Форма для выполнения работы с типами ДДС.
    '''

    class Meta:
        model = Types_operations
        fields = '__all__'
        help_text = {
            'name': 'Название типа',
        }


class CategoryForm(forms.ModelForm):
    '''
    Форма для выполнения работы с категориями ДДС.
    '''

    class Meta:
        model = Categories
        fields = '__all__'
        help_text = {
            'name': 'Название категории',
            'type_operation': 'Тип операции'
        }


class SubcategoryForm(forms.ModelForm):
    '''
    Форма для выполнения работы с подкатегориями ДДС.
    '''

    class Meta:
        model = Subcategories
        fields = ['name', 'category']
        help_text = {
            'name': 'Название подкатегории',
            'categpry': 'Связан с категорией'
        }
    