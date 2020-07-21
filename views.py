from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def bmipage(request):
    return render(request,"bmi.html")
def getdata(request):
    wt=request.GET['Weight']
    ht=request.GET['Height']
    wtf=float(wt)
    htf=float(ht)
    BMI = wtf/(htf**2)    
    return render(request,"valid.html",{"Weight":wt,"Height":ht,"Wtf":wtf,"Htf":htf,"bmi":BMI})