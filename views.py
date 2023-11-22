from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hello(request):
    return HttpResponse("Hello Django")

def home_page(request):
    context = {
        "submit" : False
    }
    if request.method == 'POST' :
        context ["submit"] =  True
        data = request.POST
        long_url = data['longurl']
        custom = data['custom_name']
        print(long_url)
        print(custom)
    else :
        print("No data received")
    return render(request,"index.html",context)
    