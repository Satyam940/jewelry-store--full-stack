from django.core.management.base import BaseCommand
from django.core import management
import os

class Command(BaseCommand):
    help = 'Loads initial data from a JSON file'

    def handle(self, *args, **options):
        fixture_file = 'store/data.json'
        if os.path.exists(fixture_file):
            management.call_command('loaddata', fixture_file)
            self.stdout.write(self.style.SUCCESS('Successfully loaded data'))
        else:
            self.stdout.write(self.style.ERROR('Fixture file not found'))