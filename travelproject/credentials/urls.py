from . import views
from django.urls import path

urlpatterns = [

    path('register',views.register,name='register'),
    # path("add/",views.addition,name='addition'),
    # path('contact/',views.contact,name='contact')
]
