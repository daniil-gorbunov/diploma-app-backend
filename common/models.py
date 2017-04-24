from django.db.models import (
    BooleanField, CharField, DateTimeField, DecimalField, ForeignKey, IntegerField, ManyToManyField, Model, TextField
)
from django.contrib.auth.models import User


class Seller(Model):
    name = CharField(max_length=255)
    is_enabled = BooleanField(default=True)


class SellerFeedback(Model):
    text = TextField()
    is_enabled = BooleanField(default=True)
    created_at = DateTimeField(auto_now_add=True)
    seller = ForeignKey(Seller)
    user = ForeignKey(User)


class DishCategory(Model):
    name = CharField(max_length=255)


class Dish(Model):
    name = CharField(max_length=255)
    description = TextField(default='')
    weight = IntegerField(default=0)
    price = DecimalField(max_digits=11, decimal_places=2)
    image = CharField(max_length=255)
    is_enabled = BooleanField()
    category = ForeignKey(DishCategory)


class Order(Model):
    STATUS_ORDERING = 1
    STATUS_PROCESSING = 2
    STATUS_DELIVERING = 3
    STATUS_COMPLETED = 4

    STATUS_CHOICES = (
        (STATUS_ORDERING, 'Ordering'),
        (STATUS_PROCESSING, 'Processing'),
        (STATUS_DELIVERING, 'Delivering'),
        (STATUS_COMPLETED, 'Completed'),
    )

    status = IntegerField(default=STATUS_ORDERING, choices=STATUS_CHOICES)
    feedback = TextField(null=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)
    user = ForeignKey(User)
    dishes = ManyToManyField(Dish, through='OrderDish')


class OrderDish(Model):
    price = DecimalField(max_digits=11, decimal_places=2)
    order = ForeignKey(Order)
    dish = ForeignKey(Dish)
