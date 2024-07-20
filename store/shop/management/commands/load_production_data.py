from django.core.management.base import BaseCommand
from django.core import management
import traceback
import sys

class Command(BaseCommand):
    help = 'Loads production data from a JSON file'

    def handle(self, *args, **options):
        try:
            management.call_command('migrate')
            self.stdout.write("Migrations complete")

            fixture_file = 'store/data.json'
            management.call_command('loaddata', fixture_file)
            self.stdout.write(self.style.SUCCESS(f"Data loaded successfully from {fixture_file}"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"An error occurred: {str(e)}"))
            self.stderr.write(self.style.ERROR(traceback.format_exc()))