from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel
from user.models import UserAccount
from platforms.models import Platforms


# Create your models here.
# TimeStampedModel, SoftDeletableModel esto funciona como auditoria para el control de Add, Update, delete
# Solo borrado lógico
class Contract(TimeStampedModel, SoftDeletableModel):
    # Valores que toma django tipo lista
    periodicity = [
        ('AN', 'ANUAL'),
        ('MEN', 'MENSUAL'),
    ]

    payment_period = [
        ('BAJA', 'BAJA')
    ]
    # relacion de 1:N entre usuario y contrato, plataforma y contrato
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, null=False, blank=True)
    platforms = models.ForeignKey(Platforms, on_delete=models.CASCADE, null=False, blank=True)
    amount = models.CharField(null=False, max_length=11, blank=True)
    periodicity_type = models.CharField(max_length=50, choices=periodicity, default='MEN', null=False, blank=True)
    periodicity_value = models.IntegerField(null=False, blank=True)
    next_pay_date = models.DateTimeField(auto_now_add=True)
    payment_period = models.CharField(max_length=50, choices=payment_period, default='BAJA', null=False)
    is_active = models.BooleanField(default=True)
    pay_date = models.DateTimeField(auto_now_add=True)
    is_pay = models.BooleanField(default=False)
    is_postpone = models.BooleanField(default=False)


def __str__(self):
    return self.amount
