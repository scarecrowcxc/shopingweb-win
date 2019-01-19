from rest_framework import serializers
from .models import Goods

# 对于前后端分离项目来说 这个文件很重要


# 这是最痛快的那种写法
class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = '__all__'

        # 也可以部分序列化
        # fields = ['name','add_time']



class GoodsSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=30, min_length=3)
    goods_front_image = serializers.ImageField(required=True)
    shop_price = serializers.FloatField(required=True)
    add_time = serializers.DateTimeField(required=True)