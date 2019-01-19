from rest_framework import serializers
from .models import VerifyCode, UserProfile
from gulishop.settings import MOBILE_RE
from datetime import datetime
import re


class VerifyCodeSerializer(serializers.ModelSerializer):

    def validate_mobile(self, mobile):
        # 第一步 ： 判断手机是否合法
        com = re.compile(MOBILE_RE)
        if not com.match(mobile):
            raise serializers.ValidationError('手机号码不合法')

        # 第二步：判断手机是否注册过
        if UserProfile.objects.filter(mobile=mobile):
            raise serializers.ValidationError('手机号码已经被注册')

        # 第三步：判断手机发送验证码频率
        ver_list = VerifyCode.objects.filter(mobile=mobile).order_by('-add_time')
        if ver_list:
            ver = ver_list[0]
            # 判断时间是否小于1分钟
            if datetime.now() - ver.add_time.second <= 60:
                raise serializers.ValidationError('验证码已发送，请1分钟后再次发送')
            else:
                # 把作废的验证码删掉
                ver.delete()
        return mobile   # 把这个mobile return 回去


    class Meta:
        model = VerifyCode
        fields = ['mobile']
