from django.shortcuts import render
from  django.http import HttpResponse

def infos(request):
    if request.method=="POST":
        combo = request.POST["operator"]
        print(combo)
    return HttpResponse("work")
