from django.contrib import admin

# Register your models here.
from tag.models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'states', 'create_time', 'update_time')
