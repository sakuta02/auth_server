from enum import Enum

from django.db import models


class Status(Enum):
    ALLOWED = 'Доступ разрешен'
    DENIED = 'Отказано в доступе'
    NOT_VIEWED = 'Заявка не рассмотрена'

    @classmethod
    def choices(cls):
        return [(status.value, status.value) for status in cls]


class Device(models.Model):
    device_id = models.CharField(max_length=200, primary_key=True, db_index=True)
    status = models.CharField(
        max_length=60,
        choices=Status.choices(),
        default=Status.NOT_VIEWED.value
    )
    subscription_expires_date = models.DateField(null=True, blank=True)
    last_login_date = models.DateTimeField(auto_now=True)
    registration_date = models.DateTimeField(auto_now_add=True)
