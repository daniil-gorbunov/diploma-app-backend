from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.fields import ForeignKey
from tastypie.resources import ModelResource
from common.models import Dish, DishCategory, Cafe, CafeFeedback, Order


class DishCategoryResource(ModelResource):
    class Meta:
        queryset = DishCategory.objects.all()
        resource_name = 'dish_category'
        allowed_methods = ['get']


class OrderResource(ModelResource):
    class Meta:
        queryset = Order.objects.prefetch_related('dishes').all()
        resource_name = 'order'
        allowed_methods = ['get']
        filtering = {
            'cafe': ALL_WITH_RELATIONS,
            'user': ALL_WITH_RELATIONS,
        }


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

    class Meta:
        queryset = Dish.objects.prefetch_related('category').filter(is_enabled=True).all()
        resource_name = 'dish'
        allowed_methods = ['get']
        filtering = {
            'cafe': ALL_WITH_RELATIONS,
        }
