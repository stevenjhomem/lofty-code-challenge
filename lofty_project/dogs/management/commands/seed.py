import requests
from django.core.management.base import BaseCommand

from dogs.models import DogImageSet


class Command(BaseCommand):
    help = "Get Dog seed data for database"

    def add_arguments(self, parser):
        parser.add_argument(
            '--total_dogs',
            type=int,
            help="Number of dog images to collect",
        ),

    def handle(self, *args, total_seeds, **kwargs):
        try:
            self.stdout.write('Seeding has begun.')
            response = self.get_dog_data(total_seeds)
            response.raise_for_status()
            json = response.json()
            urls_list = json['message']
            for index, url in enumerate(urls_list):

                self.stdout.write(f'Getting image {index + 1} for url: {url}')

                image_response = requests.get(url)
                image_response.raise_for_status()

                self.stdout.write(f'---Successful---')
                self.stdout.write(f'Writing image {index + 1} contents to memory and extracting metadata.')

                dog_images = DogImageSet()
                dog_images.set_default_image(image_response.content)
                dog_images.set_default_image_metadata(image_response.content)
                dog_images.save()
                self.stdout.write(f'---Successful---')
            self.stdout.write('Seeding has completed successfully. Please check admin to see newly added dog data.')
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)

    def get_dog_data(self, number_of_dogs):
        response = requests.get(f'https://dog.ceo/api/breeds/image/random/{number_of_dogs}')
        return response
