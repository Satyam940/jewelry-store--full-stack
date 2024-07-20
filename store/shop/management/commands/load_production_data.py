from django.core.management.base import BaseCommand
from django.core import management

class Command(BaseCommand):
    help = 'Loads production data from a JSON file'

    def handle(self, *args, **options):
        management.call_command('migrate')
        self.stdout.write("Migrations complete")

        fixture_file = 'store/data.json'
        management.call_command('loaddata', fixture_file)
        self.stdout.write(self.style.SUCCESS(f"Data loaded successfully from {fixture_file}"))