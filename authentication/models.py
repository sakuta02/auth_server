from datetime import date, timedelta
from enum import Enum

from django.db import models


class Status(Enum):
    ALLOWED = 'Доступ разрешен'
    DENIED = 'Отказано в доступе'
    NOT_VIEWED = 'Заявка не рассмотрена'

    @classmethod
    def choices(cls):
        return [(key.name, key.value) for key in cls]


class Device(models.Model):
    device_id = models.CharField(max_length=200, primary_key=True, db_index=True)
    status = models.CharField(max_length=20, choices=Status.choices(), default=Status.NOT_VIEWED.value)
    subscription_expires_date = models.DateField(default=None, null=True, blank=True)
    last_login_date = models.DateTimeField(auto_now=True)
    registration_date = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_one_month_sub():
        return date.today() + timedelta(days=30)

    @staticmethod
    def get_half_year_sub():
        return date.today() + timedelta(days=30 * 6)

    @staticmethod
    def get_one_year_sub():
        return date.today() + timedelta(days=30 * 12)

    @staticmethod
    def get_forever_sub():
        return date.today() + timedelta(days=30 * 600)
