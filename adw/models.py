from django.db.models import *
from django.contrib.postgres.fields import JSONField


class Form(Model):
    descriptions = JSONField()
