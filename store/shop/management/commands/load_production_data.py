from django.core.management.base import BaseCommand
from django.core import management
import json
import os

class Command(BaseCommand):
    help = 'Loads production data from a JSON file'

    def handle(self, *args, **options):
        fixture_file = 'store/data.json'
        try:
            if not os.path.exists(fixture_file):
                raise FileNotFoundError(f"The file {fixture_file} does not exist")

            with open(fixture_file, 'r', encoding='utf-16') as f:
                data = json.load(f)
            
            # Write the data back in UTF-8 encoding
            with open('temp_data.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            # Load the UTF-8 encoded data
            management.call_command('loaddata', 'temp_data.json')
            self.stdout.write(self.style.SUCCESS('Successfully loaded data'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {str(e)}'))
            raise  # Re-raise the exception to propagate it