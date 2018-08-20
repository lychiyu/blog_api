from django.contrib import admin

# Register your models here.
from categroy.models import Categroy


@admin.register(Categroy)
class CateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'states', 'create_time', 'update_time')
