import os
import traceback
from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from django.conf import settings

class Command(BaseCommand):
    help = 'Load production data from JSON file'

    def handle(self, *args, **options):
        data_file = os.path.join(settings.BASE_DIR, 'data.json')
        if not os.path.exists(data_file):
            raise CommandError(f'File {data_file} does not exist.')

        try:
            call_command('loaddata', data_file)
            self.stdout.write(self.style.SUCCESS('Successfully loaded production data'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {str(e)}'))
            traceback.print_exc(file=self.stdout)
