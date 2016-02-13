# -*- coding: utf-8 -*-
# Copyright (c) 2016 Aladom SAS & Hosting Dvpt SAS
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help= """Do nothing"""

    def handle(self, *args, **options):
        print("Magikarp used Splash!")
        print("It's not very effective...")
        pass
