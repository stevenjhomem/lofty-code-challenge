from django.contrib import admin

from dogs.models import DogImageSet


@admin.register(DogImageSet)
class DogAdmin(admin.ModelAdmin):
    model = DogImageSet
    list_display = [
        'default_image',
        'modified_image',
        'original_image_metadata',
        'updated_ts',
        'created_ts'
    ]
