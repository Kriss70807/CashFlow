from django.contrib import admin

from .models import Categories, Statuses, Subcategories, Types_operations

admin.site.register(Categories)
admin.site.register(Statuses)
admin.site.register(Subcategories)
admin.site.register(Types_operations)
