from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import account
# Create your views here.

def signup(request):
    count=0
    acc = account.objects.all()
    if request.method== 'POST':
        for obj in acc:
            if obj.__str__()==request.POST.get('firstname') and obj.mob()==request.POST.get('mobilenumber'):
                count=count+1
        if count<1:
                savrecord = account()
                savrecord.firstname=request.POST.get('firstname')
                savrecord.lastname=request.POST.get('lastname')
                savrecord.email=request.POST.get('email')
                savrecord.address1=request.POST.get('address1')
                savrecord.address2=request.POST.get('address2')
                savrecord.address3=request.POST.get('address3')
                savrecord.mobilenumber=request.POST.get('mobilenumber')
                savrecord.country=request.POST.get('country')
                savrecord.state=request.POST.get('state')
                savrecord.zip=request.POST.get('zip')
                savrecord.save()
        else:
            return redirect('alreadyregistered')

        return redirect('upload')

    else:
            return render(request,'accounts/signup.html')
