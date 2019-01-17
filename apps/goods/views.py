from django.shortcuts import render, HttpResponse
from .models import StudentInfo
from django.views import View
from django.core import serializers
import json
from django.http import JsonResponse


# # Create your views here.
# def student_list(request):
#     if request.method == "GET":
#         all_students = StudentInfo.objects.all()
#         return render(request, 'student_list.html', {
#             'all_students': all_students
#         })
#     else:
#         #这里处理post请求的逻辑
#
#
# class StudentListView(View):
#     def get(self, request):
#         all_students = StudentInfo.objects.all()
#         data = serializers.serialize('json', all_students)
#         data = json.loads(data)
#         return JsonResponse(data)
#
#
# class StudentDetailView(View):
#     def get(self, request, pk):
#         if pk:
#             student = StudentInfo.objects.filter(id=int(pk))
#             return render(request, 'student_detail.html', {
#                 'student': student
#             })
#
# class StudentAddView(View):
#     def post(self, request):
#         return JsonResponse({'创建好的学生'})
#
#
# class StudentUpdateView(View):
#     def post(self, request, pk):
#         return JsonResponse({'修改后的学生'})
#
#
# class StudentDeleteView(View):
#     def get(self, request, pk):
#         return JsonResponse({'返回删除成功的状态'})
#
#


class StudentsView(View):
    def get(self, request):
        all_students = StudentInfo.objects.all()
        data = serializers.serialize('json', all_students)
        data = json.loads(data)
        return JsonResponse(data, safe=False, status=200)

    def post(self, request):
        pass
        return HttpResponse('添加成功的对象json', status=201)


class StudentsSingle(View):
    def get(self, request, pk):
        student = StudentInfo.objects.filter(id=int(pk))
        data = serializers.serialize('json', student)
        data = json.loads(data)
        return JsonResponse(data, status=200, safe=False)

    def delete(self, request, pk):
        StudentInfo.objects.filter(id=int(pk)).delete()
        return JsonResponse({}, status=204, safe=False)

    def put(self, request, pk):
        pass
        return HttpResponse('修改成功的对象json', status=201)

    def patch(self, request, pk):
        pass
        return HttpResponse('修改成功的对象json', status=201)












