import sys
sys.path.append('/../leak')
# from models import Category, CATEGORIES

import models

from django.core.management.base import BaseCommand
# import get or 404


class Command(BaseCommand):
    help = "This command is used to create categories"

    # def add_arguments(self, parser):
        # parser.add_argument('username', type=str, help='Enter the username')
        # parser.add_argument('password', type=str, help='Enter the password')


    def handle(self, *args, **kwargs):
        # username = kwargs['username']
        # password = kwargs['password']

        # if username and password:
        #     testuser = User.objects.get_or_404(username=username) or None
        #     if testuser:
        #         self.stdout.write(f"The user {username} has already been chosen!\n\tchoose another name and recreate!")
        #         return

        #     user = User.objects.create_user(username=username, password=password)
            
        #     self.stdout.write(f"The user {username} has been created!")
        for cat in  models.CATEGORIES:
            category = models.Category.objects.create(title=cat, description='Add the description later!')

            self.stdout.write(f"{category} has been created!")