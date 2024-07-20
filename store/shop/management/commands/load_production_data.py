# from django.core.management.base import BaseCommand
# from django.core import management
# from django.apps import apps
# import json

# class Command(BaseCommand):
#     help = 'Loads production data from a JSON file'

#     def handle(self, *args, **options):
#         try:
#             management.call_command('migrate')
#             self.stdout.write("Migrations complete")

#             fixture_file = 'store/data.json'
#             temp_file = 'store/data_utf8.json'

#             # Try different encodings
#             encodings = ['utf-8', 'utf-16', 'iso-8859-1', 'windows-1252']
            
#             for encoding in encodings:
#                 try:
#                     with open(fixture_file, 'r', encoding=encoding) as f:
#                         data = json.load(f)
#                     self.stdout.write(f"Successfully read file with {encoding} encoding")

#                     # Convert data to utf-8 and save to a temporary file
#                     with open(temp_file, 'w', encoding='utf-8') as temp_f:
#                         json.dump(data, temp_f, ensure_ascii=False, indent=4)
#                     self.stdout.write(f"Converted data to utf-8 and saved to {temp_file}")
#                     break
#                 except UnicodeDecodeError:
#                     continue
#             else:
#                 raise ValueError("Unable to decode the file with any of the attempted encodings")

#             self.stdout.write(f"Found {len(data)} objects in {fixture_file}")

#             for item in data:
#                 self.stdout.write(f"Loading {item['model']} with pk {item['pk']}")

#             management.call_command('loaddata', temp_file)
#             self.stdout.write(self.style.SUCCESS(f"Data loaded successfully from {temp_file}"))

#             # Print out the number of objects for each model
#             for model in apps.get_models():
#                 count = model.objects.count()
#                 self.stdout.write(f"{model.__name__}: {count} objects")

#         except Exception as e:
#             self.stderr.write(self.style.ERROR(f"An error occurred: {str(e)}"))
#             import traceback
#             self.stderr.write(self.style.ERROR(traceback.format_exc()))
