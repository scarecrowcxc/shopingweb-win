
from django_filters import rest_framework as filters
from .models import Goods

class GoodsFilter(filters.FilterSet):
    minprice = filters.NumberFilter(field_name='shop_price',lookup_expr='gte',label='最低价格')
    maxprice = filters.NumberFilter(field_name='shop_price',lookup_expr='lte',label='最高价格')
    # name = filters.CharFilter(field_name='name',lookup_expr='contains')

    class Meta:
        model = Goods
        fields = ['minprice','maxprice']
