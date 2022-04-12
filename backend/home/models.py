from django.conf import settings
from django.db import models


class Name(models.Model):
    "Generated Model"
    name = models.BigIntegerField()
