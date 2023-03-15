import time

from django.core.management.base import BaseCommand

from keys.models import Key


class Command(BaseCommand):
    help = 'Increment all keys that have already been incremented.'

    def handle(self, *args, **options):
        while True:
            self.stdout.write('Incrementing service has begun.')
            keys = Key.objects.filter(value__gt=0)
            for key in keys:
                key.value += 1
            Key.objects.bulk_update(keys, ['value'])  # bulk update is an atomic transaction now. (https://github.com/django/django/blob/stable/4.0.x/django/db/models/query.py#L640)
            self.stdout.write(f'Incrementing service has finished. Updated {keys.count()} keys. Sleeping for 60 seconds.')
            time.sleep(60)
