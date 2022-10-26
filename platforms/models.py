from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel


# Create your models here.
# TimeStampedModel, SoftDeletableModel esto funciona como auditoria para el control de Add, Update, delete
# Solo borrado lógico
class Platforms(TimeStampedModel, SoftDeletableModel):
    name = models.CharField(max_length=50, unique=True, null=False, blank=True)


def __str__(self):
    return self.name
