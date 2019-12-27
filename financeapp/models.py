from django.db import models


class Expense(models.Model):
    amount = models.FloatField()

    def __str__(self):
        return str(self.amount)


class Income(models.Model):
    amount = models.FloatField()

    def __str__(self):
        return str(self.amount)
