from unicodedata import name
from django.shortcuts import render, HttpResponse
import requests
import urllib.parse
name_api = 'http://dxx.ahyouth.org.cn/api/peopleRankStage?'
table_api = "http://dxx.ahyouth.org.cn/api/peopleRankList"
table_number = requests.get(table_api).json()["list"][0]["table_name"]  


def index(request):
    return render(request,"index.html")

def help(request):
    return render(request,"help.html")

def donate(request):
    return render(request,"donate.html")

def qr(request):
    base =  urllib.parse.unquote(request.POST.get('url')).split('?')[1]
    url =  'http://47.113.204.212:81/query?' + base
    level = urllib.parse.unquote(base)
    return render(request,"qr.html",{'url':url,'level':level})

def update(request):
    return render(request,"update.html")

def query(request):
    query_str = ''
    all_name = []
    done_name = []
    query = request.GET
    for key in query:
        query_str += key + '=' + query[key] + '&'
    all = requests.get(name_api + query_str).json()["list"]["list"]
    for item in all:
        all_name.append(item['username'])
    done = requests.get(name_api + 'table_name=' + table_number +query_str[26:]).json()["list"]["list"]
    for item in done:
        done_name.append(item['username'])

    undo_name = list(set(all_name).difference(set(done_name)))
    num = len(undo_name)
    return render(request,"query.html",{'name':undo_name,'num':num})
