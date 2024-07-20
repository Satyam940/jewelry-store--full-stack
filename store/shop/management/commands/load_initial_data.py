from django.core.management.base import BaseCommand
from django.core import management
import os
import traceback
import sys

class Command(BaseCommand):
    help = 'Loads initial data from a JSON file'

    def handle(self, *args, **options):
        try:
            fixture_file = 'store/data.json'
            self.stdout.write(f"Attempting to load data from: {os.path.abspath(fixture_file)}")
            
            if os.path.exists(fixture_file):
                self.stdout.write("Fixture file found. Attempting to load data.")
                management.call_command('loaddata', fixture_file)
                self.stdout.write(self.style.SUCCESS('Successfully loaded data'))
            else:
                self.stdout.write(self.style.ERROR(f'Fixture file not found at {os.path.abspath(fixture_file)}'))
        except Exception as e:
            error_info = sys.exc_info()
            error_tb = traceback.format_exception(*error_info)
            self.stderr.write(f"Error: {str(e)}\n\nTraceback:\n{''.join(error_tb)}")