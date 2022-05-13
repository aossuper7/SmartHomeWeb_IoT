from django.shortcuts import render
from django.views import View
from django_request_mapping import request_mapping
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from iotweb.models import User
import json
@request_mapping("")
class MyView(View):

    @request_mapping("/", method="get")
    def home(self, request):
        return render(request, 'login.html')

    @request_mapping("loginok/", method="get")
    def index(self, request):
        return render(request, 'index.html')

    @request_mapping("/cctv", method="get")
    def cctv(self, request):
        return render(request, 'cctv.html')

    @request_mapping("/forgot-password", method="get")
    def forgot_password(self, request):
        return render(request, 'forgot-password.html')

    @request_mapping("/register", method="get")
    def register(self, request):
        return render(request, 'register.html')

    @request_mapping("/login", method="post")
    def login(self, request):
        if request.method == 'POST':
            print("request_ok")
            data = JSONParser().parse(request)
            user_id = data["user_id"]
            print(data)
            obj = User.objects.get()
            if obj.user_id != user_id:
                return JsonResponse("fail", safe=False, json_dumps_params={'ensure_ascii': False})
            if data["user_pwd"] == obj.user_pwd:
                return JsonResponse("ok", safe=False, json_dumps_params={'ensure_ascii': False})
            else:
                return JsonResponse("fail", safe=False, json_dumps_params={'ensure_ascii': False})