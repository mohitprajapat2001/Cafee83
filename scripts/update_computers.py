# -*- coding: utf-8 -*-
import os
import sys
import django

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cafee83.settings")
django.setup()

from cafehome.models import Computer

if __name__ == "__main__":
    computers = Computer.objects.all()
    for computer in computers:
        computer.status = 1
        computer.save()
