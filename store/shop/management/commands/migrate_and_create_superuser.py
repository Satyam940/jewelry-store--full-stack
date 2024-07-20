from django.core.management.base import BaseCommand
from django.core import management
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Runs migrations and creates a superuser if one doesn\'t exist'

    def handle(self, *args, **options):
        management.call_command('migrate')
        self.stdout.write(self.style.SUCCESS('Migrations completed successfully'))

        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser('satyam', 'satyam@gmail.com', 'satyam')
            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
        else:
            self.stdout.write(self.style.SUCCESS('Superuser already exists'))   