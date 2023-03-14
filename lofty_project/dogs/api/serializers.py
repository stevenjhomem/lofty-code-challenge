from rest_framework import serializers

from dogs.models import DogImageSet


class DogImageSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DogImageSet
        fields = [
            'id',
            'default_image',
            'modified_image',
            'original_image_metadata'
        ]
        read_only_fields = ('id',)
