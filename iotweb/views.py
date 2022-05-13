from django.shortcuts import render
from django.views import View
from django_request_mapping import request_mapping
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from iotweb.models import User
from datetime import datetime
import json

humidSetData = {}
tempSetData = {}

def FileSet(name, dic, data):
    now = datetime.now()
    current_time = now.strftime("%H/%M/%S")
    if len(dic) > 19:
        dic.pop(next(iter(dic))) #첫번째 값 제거
    dic[current_time] = data
    with open(name, "w") as f:
        json.dump(dic, f)
    f.close()

def FileRead(name):
    try:
        with open(name, "r") as f:
            return json.load(f)
    except:
        print("파일없음")
        f = open(name, "w")
    finally:
        f.close()

@request_mapping("")
class MyView(View):

    @request_mapping("/home", method="get")
    def home(self, request):
        jsonHumid = FileRead("humid.json")
        jsonTemp = FileRead("temp.json")
        data = {'jsonHumid': jsonHumid, 'jsonTemp': jsonTemp}
        return render(request, 'index.html', {'dht' : data})

    @request_mapping("loginok/", method="get")
    def index(self, request):
        return render(request, 'index.html')

    @request_mapping("/cctv", method="get")
    def cctv(self, request):
        return render(request, 'cctv.html')
      
    @request_mapping("/dataset", method="get")
    def dataset(self, request):
        humid = request.GET.get('humid')
        temp = request.GET.get('temp')
        humidSetData = FileRead("humid.json")
        tempSetData = FileRead("temp.json")
        FileSet("humid.json", humidSetData, humid)
        FileSet("temp.json", tempSetData, temp)
        return JsonResponse({"result": 1})


    @request_mapping("/", method="get")
    def login(self, request):
        return render(request, 'login.html')

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



