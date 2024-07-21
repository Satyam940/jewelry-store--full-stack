from django.core.management.base import BaseCommand
from django.core import management
import os

class Command(BaseCommand):
    help = 'Populate the database with initial data'

    def handle(self, *args, **options):
        # Check if the data has already been loaded
        from django.contrib.auth.models import User
        if User.objects.count() == 0:
            fixture_file = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), 'data.json')
            if os.path.exists(fixture_file):
                try:
                    management.call_command('loaddata', fixture_file)
                    self.stdout.write(self.style.SUCCESS(f"Data loaded successfully from {fixture_file}"))
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Failed to load data: {str(e)}"))
            else:
                self.stderr.write(self.style.WARNING(f"Fixture file {fixture_file} not found"))
        else:
            self.stdout.write(self.style.SUCCESS("Database already contains data, skipping initial load"))