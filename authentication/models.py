from django.db import models
from enum import Enum


class Status(Enum):
    ALLOWED = 'Доступ разрешен'
    DENIED = 'Отказано в доступе'
    NOT_VIEWED = 'Заявка не рассмотрена'

    @classmethod
    def choices(cls):
        return [(key.name, key.value) for key in cls]


class Device(models.Model):
    device_id = models.SlugField(primary_key=True, db_index=True)
    status = models.CharField(max_length=20, choices=Status.choices(), default=Status.NOT_VIEWED.value)
    registration_date = models.DateTimeField(auto_now_add=True)
    last_login_date = models.DateTimeField(auto_now=True)
