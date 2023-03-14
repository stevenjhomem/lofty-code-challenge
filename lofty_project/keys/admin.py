from django.contrib import admin

from keys.models import Key


@admin.register(Key)
class DogAdmin(admin.ModelAdmin):
    model = Key
    list_display = [
        'name',
        'value',
    ]
