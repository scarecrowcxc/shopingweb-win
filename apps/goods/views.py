from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views import View
from .models import Goods
import json
from django.forms.models import model_to_dict
from django.core import serializers
from .serializers import GoodsSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, mixins


# 第一种方式， 自己用python最原始的方式去序列化，但是对于图片序列化的时候， 不支持json序列化
# class GoodsView(View):
#     def get(self, request):
#         all_goods = Goods.objects.all()
#         items = []
#         for goods in all_goods:
#             item = {}
#             item['name'] = goods.name
#             item['shop_price'] = goods.shop_price
#             # item['goods_front_image'] = goods.goods_front_image
#             items.append(item)
# 使用HttpResponse返回 需要先去把python的json格式类型转化为json的字符串
# data = json.dumps(items)
# return HttpResponse(data, content_type='application/json')

# 使用JsonResponse
# return JsonResponse(items, safe=False)

# 第二种方式, 使用Django当中封装的model_to _dict方法一次性全部序列化， 但是他只是对我们的第一种方式的简化 并未解决图片序列化不了的问题
# class  GoodsView(View):
#     def get(self, request):
#         all_goods = Goods.objects.all()
#         items = []
#         for goods in all_goods:
#             item = model_to_dict(goods)
#             items.append(item)
#         # data = json.dumps(items)
#         # return HttpResponse(data, content_type='application/json')
#
# return JsonResponse(items, safe=False)


# 第三种方式， 使用Django的serializers去做序列化， 它就已经帮我们把图片无法序列化的问题解决了
# class GoodsView(View):
#     def get(self, request):
#         all_goods = Goods.objects.all()
#         data = serializers.serialize('json', all_goods)
#
#         # json.loads()是将Json格式 转成 python格式字典
#         # 因为JsonResponse()的参数要的是 python格式字典
#         data = json.loads(data)
#         return JsonResponse(data, safe=False)


######引入 Django REST framework ###### 使用更NB的View
# class GoodsView(APIView):
#     '''
#         使用drf最基础的APIView实现商品列表的数据接口
#     '''
#
#     def get(self, request):
#         # 拿到要返给前端的数据
#         all_goods = Goods.objects.all()
#
#         # 进行序列化 第一个参数是待序列化的数据，要求queryset类型。 得到一个序列化好后的对象实例
#         serializer = GoodsSerializer(all_goods, many=True)
#
#         return Response(data=serializer.data, status=status.HTTP_200_OK)


class GoodsView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
