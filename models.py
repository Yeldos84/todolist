from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator

class TodoUsers(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=10, validators=[MinLengthValidator(limit_value=6, message=">6")])

    def __str__(self):
        return self.login


class TodoModelCreate(models.Model):
    add = models.CharField(max_length=20)

    def __str__(self):
        return self.add