from django.shortcuts import render

def homepage(request):
    return render(request,'home.html')

def successful(request):
    return render(request,'successful.html')

def about(request):
    return render(request,'about.html')

def alreg(request):
    return render(request,'alreadyregistered.html')

def instr(request):
    return render(request,'instructions.html')
