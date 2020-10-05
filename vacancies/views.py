from django.shortcuts import render
from .models import Vacancy
# Create your views here.
def vacancy(request):
    vacancy=Vacancy.objects
    return render(request,'vacancies/vacancy.html',{'vacancy':vacancy})
