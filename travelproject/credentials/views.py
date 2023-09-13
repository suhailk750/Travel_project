# from django.http import HttpResponse
from django.contrib import message, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def register(request):
    if request.method=='POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        c_password = request.POST['confirm_password']
        if password==c_password:
            if User.objects.filter(username=username).exists():
                message.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                message.info(request,'email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password
                )
                user.save()
            print("user created")
        else:
            messages.info(request, 'password not matched')
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")












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