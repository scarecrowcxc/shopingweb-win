from rest_framework import serializers
from .models import Goods


# class GoodsSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True,max_length=30,min_length=3)
#     goods_front_image = serializers.ImageField(required=True)
#     shop_price = serializers.FloatField(required=True)
#     add_time = serializers.DateTimeField(required=True)


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        #可以部分序列化
        # fields = ['name','add_time']
        #可以全部序列化
        fields = '__all__'
