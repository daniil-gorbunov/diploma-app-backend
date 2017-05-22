from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.fields import ForeignKey, IntegerField, ToManyField
from tastypie.resources import ModelResource
from django.contrib.auth.models import User
from common.models import Dish, DishCategory, Cafe, CafeFeedback, Order
from common.api.authorization import AllowAllAuthorization


class DishCategoryResource(ModelResource):

    class Meta:
        queryset = DishCategory.objects.all()
        resource_name = 'dish_category'
        allowed_methods = ['get']


class CafeResource(ModelResource):

    class Meta:
        queryset = Cafe.objects.filter(is_enabled=True).all()
        resource_name = 'cafe'
        allowed_methods = ['get']
        filtering = {
            'id': ALL,
        }


class CafeFeedbackResource(ModelResource):

    class Meta:
        queryset = CafeFeedback.objects.all()
        resource_name = 'cafe_feedback'
        allowed_methods = ['get']
        filtering = {
            'cafe': ALL_WITH_RELATIONS,
        }


class DishResource(ModelResource):
    cafe = ForeignKey(CafeResource, 'cafe')
    category = ForeignKey(DishCategoryResource, 'category', full=True)
    quantity = IntegerField(default=0)

    class Meta:
        queryset = Dish.objects.prefetch_related('category').filter(is_enabled=True).all()
        resource_name = 'dish'
        allowed_methods = ['get']
        filtering = {
            'cafe': ALL_WITH_RELATIONS,
        }


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        allowed_methods = ['get']


class OrderResource(ModelResource):
    user = ForeignKey(UserResource, 'user')
    cafe = ForeignKey(CafeResource, 'cafe')
    dishes = ToManyField(DishResource, 'dishes', full=True)

    class Meta:
        queryset = Order.objects.prefetch_related('dishes').all()
        resource_name = 'order'
        allowed_methods = ['get', 'post']
        filtering = {
            'cafe': ALL_WITH_RELATIONS,
            'user': ALL_WITH_RELATIONS,
        }
        authorization = AllowAllAuthorization()
