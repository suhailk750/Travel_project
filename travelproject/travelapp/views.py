# from django.http import HttpResponse
from django.shortcuts import render
from . models import place,team
# Create your views here.
def demo(request):
    obj=place.objects.all()
    ob=team.objects.all()

    return render(request,"index.html",{'result':obj,'res':ob})


















# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     res2 =x*y
#     res3 =x/y
#     return render(request,"result.html",{'num1': x, 'num2': y, 'result': res, 'res2': res2, 'res3': res3})
# def about(request):
#     return render(request,"about.html")

# def contact(request):
#     return HttpResponse("Hello contact")