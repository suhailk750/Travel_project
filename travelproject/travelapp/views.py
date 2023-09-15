from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from . models import place,team
# Create your views here.
def demo(request):
    obj=place.objects.all()
    ob=team.objects.all()

    return render(request,"index.html",{'result':obj,'res':ob})
