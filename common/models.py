from django.db.models import (
    BooleanField,
    CharField,
    DateTimeField,
    DecimalField,
    ForeignKey,
    IntegerField,
    ManyToManyField,
    Model,
    PositiveSmallIntegerField,
    TextField,
)
from django.contrib.auth.models import User


class Cafe(Model):
    name = CharField(max_length=255)
    phone = CharField(max_length=255, null=True, blank=True)
    logo = CharField(max_length=255, null=True, blank=True)
    is_enabled = BooleanField(default=True)


class CafeFeedback(Model):
    text = TextField()
    is_enabled = BooleanField(default=True)
    created_at = DateTimeField(auto_now_add=True)
    cafe = ForeignKey(Cafe)
    user = ForeignKey(User)


class DishCategory(Model):
    name = CharField(max_length=255)


class Dish(Model):
    name = CharField(max_length=255)
    description = TextField(default='', null=True, blank=True)
    weight = CharField(max_length=100, default='', null=True, blank=True)
    price = DecimalField(max_digits=11, decimal_places=2)
    image = CharField(max_length=255, null=True, blank=True)
    is_enabled = BooleanField()
    category = ForeignKey(DishCategory)
    cafe = ForeignKey(Cafe)


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
    comment = TextField(null=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)
    user = ForeignKey(User)
    cafe = ForeignKey(Cafe)
    dishes = ManyToManyField(Dish, through='OrderDish')


class OrderDish(Model):
    quantity = PositiveSmallIntegerField(default=1)
    price = DecimalField(max_digits=11, decimal_places=2, default=0)
    order = ForeignKey(Order)
    dish = ForeignKey(Dish)
