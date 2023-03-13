from django.db import models


class Key(models.Model):
    name = models.TextField(null=False, blank=False, verbose_name='Name')
    value = models.IntegerField(null=False, blank=False, default=0, verbose_name='Value')

    def increment(self):
        self.value += 1
        self.save()
