import time

from django.core.management.base import BaseCommand
from django.db.models import F

from keys.models import Key


class Command(BaseCommand):
    help = 'Increment all keys that have already been incremented.'

    def handle(self, *args, **options):
        while True:
            self.stdout.write('Incrementing service has begun.')
            queryset = Key.objects.filter(value__gt=0).values_list('id', flat=True)
            number_updated = queryset.bulk_update(value=F("value") + 1, batch_size=300)  # bulk update is an atomic transaction now.
            self.stdout.write(f'Incrementing service has finished. Updated {number_updated} of keys. Sleeping for 6 seconds.')
            time.sleep(6)
