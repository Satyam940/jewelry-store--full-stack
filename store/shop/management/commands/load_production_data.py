from django.core.management.base import BaseCommand
from django.core.management import call_command
import os

class Command(BaseCommand):
    help = 'Load data from data.json into the database'

    def handle(self, *args, **kwargs):
        data_file = os.path.join(os.path.dirname(__file__), '../../../data.json')
        call_command('loaddata', data_file)
