from tastypie.resources import ModelResource
from common.models import Dish, DishCategory, Seller, SellerFeedback, Order


class DishResource(ModelResource):
    class Meta:
        queryset = Dish.objects.prefetch_related('category').all()
        resource_name = 'dish'
        allowed_methods = ['get']


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


class SellerResource(ModelResource):
    class Meta:
        queryset = Seller.objects.all()
        resource_name = 'seller'
        allowed_methods = ['get']


class SellerFeedbackResource(ModelResource):
    class Meta:
        queryset = SellerFeedback.objects.all()
        resource_name = 'seller_feedback'
        allowed_methods = ['get']
