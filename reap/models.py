from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
import pytz

# Create your models here.

class Business(models.Model):
    info = models.OneToOneField(User)
    name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=15)
    mid = models.CharField(max_length=100)
    radius = models.FloatField(default=1.0)
    ach_token = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    apple_pay = models.CharField(max_length=100)
    businesses = models.ManyToManyField(Business, related_name="customers")
    ach_token = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    buyer = models.ForeignKey(Customer)
    merchant = models.ForeignKey(Business)
    amount = models.FloatField()
    when = models.DateTimeField()

class Reward(models.Model):
    business = models.ForeignKey(Business)
    customers = models.ManyToManyField(Customer, related_name="rewards")
    title = models.CharField(max_length=50)
    amount_spent = models.FloatField(blank=True)
    discount_dollars = models.FloatField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    details = models.TextField(default='')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-end_date',)