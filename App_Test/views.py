from django.shortcuts import render, HttpResponse
import requests

# Create your views here.
from requests import Response


# def index(request):
#     return HttpResponse("欢迎使用")
#
# def user_list(request):
#     return render(request,"user_list.html")
#
# def user_add(request):
#     return HttpResponse("添加用户")
#
# def tpl(request):
#     name="王群"
#     role=["王群1","王群2","wangqun"]
#     user_info={"name":"wangqun","salary":10000,"role":"ceo"}
#     data_list=[
#         {"name": "wangqun1", "salary": 10000, "role": "ceo1"},
#         {"name": "wangqun2", "salary": 10000, "role": "ceo2"},
#         {"name": "wangqun3", "salary": 10000, "role": "ceo3"},
#     ]
#     return render(request,"tpl.html",{"n1":name,"n2":role,"n3":user_info,"n4":data_list})
#
# def news(request):
#     #定义一些新闻，或者去数据库，或者网络请求去获取联通新闻
#     # 向这个地址发送请求
#     # http://www.chinaunicom.com.cn/api/article/NewsByIndex/4/2022/03/news
#     res = requests.get("https://search.sina.com.cn/?q=阿里巴巴&c=news")
#     data_list = res.json()
#    # print(data_list)
#     return render(request,'news.html')
#
def login(request):
      return render(request,"login.html")

def news(request):
      return render(request,"news.html")
