import time
from io import BytesIO

from PIL import Image
from django.core.files import File
from django.db import models


class DogImageSet(models.Model):
    created_ts = models.DateTimeField(auto_now_add=True, verbose_name='Created Timestamp')
    updated_ts = models.DateTimeField(auto_now=True, verbose_name='Updated Timestamp')
    default_image = models.ImageField(null=False, blank=False, verbose_name='Original Image')
    modified_image = models.ImageField(null=True, blank=True, verbose_name='Modified Image')
    original_image_metadata = models.JSONField(null=False, blank=False, default=dict, verbose_name='Original Image Metadata')

    def set_default_image(self, image_data: bytes):
        file_name = f'{time.time_ns()}.jpg'
        self.default_image.save(file_name, File(BytesIO(image_data)))

    def modify_default_image(self):
        image = Image.open(self.default_image.path)
        image = image.rotate(angle=90)

        file_name, extension = self.default_image.name.split('.')[-2:]
        file_name = f'{file_name}_modified.{extension}'

        in_memory_file = BytesIO()
        image.save(in_memory_file, format='jpeg')

        self.modified_image.save(file_name, File(in_memory_file))

    def set_default_image_metadata(self, image_data: bytes):
        image = Image.open(BytesIO(image_data))
        meta_data = dict(image.getexif())
        self.original_image_metadata = meta_data
