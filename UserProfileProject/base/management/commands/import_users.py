'''customize managment commands classes'''

import csv
from django.core.management.base import BaseCommand
from base.models import User

class Command(BaseCommand):
    '''customize command to create new users from csv file'''
    help = "import new users from the csv file"

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        with open(csv_file,encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                name, email = row
                user, created = User.objects.get_or_create(username=name, email=email)
                user.set_password('123') #default password for new user
                user.save()

                if created:
                    self.stdout.write(f'User "{name}" with email "{email}" created successfully!')
                else:
                    self.stdout.write(f'User "{name}" with email "{email}" already exists!')
