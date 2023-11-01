from django.shortcuts import render
from . models import Place
from . models import team

def demo(request):
    obj = Place.objects.all()
    data = team.objects.all()
    return render(request,"index.html",{'result':obj,'team':data})


