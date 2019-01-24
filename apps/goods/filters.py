from django_filters import rest_framework as filters
from .models import Goods
from django.db.models import Q


class GoodsFilter(filters.FilterSet):
    pricemin = filters.NumberFilter(field_name='shop_price', lookup_expr='gte', label='最低价格')
    pricemax = filters.NumberFilter(field_name='shop_price', lookup_expr='lte', label='最高价格')
    # 下面这个属于模糊查找的功能，这里虽然可以做，
    # 但其实不属于过滤的功能， 一般不放在这里处理,是放在搜索功能里去做的
    # name = filters.CharFilter(field_name='name', lookup_expr='contains')

    # 自定义过滤方法method进行过滤
    top_category = filters.NumberFilter(method='get_top_category')

    # 参数value：拿到的就是top_category传过来的值
    # 参数queryset：过滤那个model拿到的就是那个model的queryset, 那么 这个queryset是个什么呢
    # 参数name：name说的是一个键 这里没用据说， 但是要写上，三个参数是位置传参， 不能乱了顺序
    def get_top_category(self, queryset, name, value):
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(
            category__parent_category__parent_category_id=value))

    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax']
