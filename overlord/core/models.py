from django.db import models
from django.core.validators import MinLengthValidator


class NamedModel(models.Model):
    name = models.SlugField(max_length=45, validators=[MinLengthValidator(1)])

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class DatedModel(models.Model):
    created = models.DateTimeField('created', auto_now_add=True)
    last_modified = models.DateTimeField('last modified', auto_now=True)

    class Meta:
        abstract = True
