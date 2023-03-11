from django.db import models


class DogImages(models.Model):
    created_ts = models.DateTimeField(auto_now_add=True, verbose_name='Created Timestamp')
    updated_ts = models.DateTimeField(auto_now=True, verbose_name='Updated Timestamp')
    original_image = models.ImageField(null=False, blank=False, verbose_name='Original Image')
    modified_image = models.ImageField(null=True, blank=True, verbose_name='Modified Image')
    original_image_metadata = models.JSONField(null=False, blank=False, default=dict, verbose_name='Original Image Metadata')

    def set_original_image(self, image_data: bytes):
        pass

    def modify_original_image(self):
        pass

    def set_original_image_metadata(self, image_data: bytes):
        pass
