from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.fields import ForeignKey, ToManyField
from tastypie.resources import ModelResource
from django.contrib.auth.models import User
from common.models import Dish, DishCategory, Cafe, CafeFeedback, Order, OrderDish
from common.api.authorization import AllowAllAuthorization


class DishCategoryResource(ModelResource):

    class Meta:
        queryset = DishCategory.objects.all()
        resource_name = 'dish_category'
        allowed_methods = ['get', 'post']
        authorization = AllowAllAuthorization()


class CafeResource(ModelResource):

    class Meta:
        queryset = Cafe.objects.filter(is_enabled=True).all()
        resource_name = 'cafe'
        allowed_methods = ['get']
        filtering = {
            'id': ALL,
        }
        authorization = AllowAllAuthorization()


class CafeFeedbackResource(ModelResource):

    class Meta:
        queryset = CafeFeedback.objects.all()
        resource_name = 'cafe_feedback'
        allowed_methods = ['get']
        filtering = {
            'cafe': ALL_WITH_RELATIONS,
        }
        authorization = AllowAllAuthorization()


class DishResource(ModelResource):
    cafe = ForeignKey(CafeResource, 'cafe')
    category = ForeignKey(DishCategoryResource, 'category', full=True)

    class Meta:
        queryset = Dish.objects.prefetch_related('category').filter(is_enabled=True).all()
        resource_name = 'dish'
        allowed_methods = ['get']
        filtering = {
            'cafe': ALL_WITH_RELATIONS,
        }
        authorization = AllowAllAuthorization()


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        allowed_methods = ['get']
        authorization = AllowAllAuthorization()


class OrderResource(ModelResource):
    user = ForeignKey(UserResource, 'user', full=True)
    cafe = ForeignKey(CafeResource, 'cafe')
    dishes = ToManyField(DishResource, 'dishes', full=True)

    class Meta:
        queryset = Order.objects.prefetch_related('dishes', 'user').filter(status=Order.STATUS_ORDERING).all()
        resource_name = 'order'
        allowed_methods = ['get', 'post']
        filtering = {
            'cafe': ALL_WITH_RELATIONS,
            'user': ALL_WITH_RELATIONS,
        }
        authorization = AllowAllAuthorization()

    def save_m2m(self, bundle):
        for field_name, field_object in self.fields.items():
            if not getattr(field_object, 'is_m2m', False):
                continue

            if not field_object.attribute:
                continue

            for field in bundle.data[field_name]:
                dish = Dish.objects.get(pk=field.data['dish_id'])
                OrderDish.objects.get_or_create(
                    dish=dish,
                    order=bundle.obj,
                    quantity=field.data['quantity'],
                    price=dish.price
                )
