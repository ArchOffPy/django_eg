from django.shortcuts import render
from django.http import HttpResponse

def monday(request):
    return HttpResponse('Начать изучать DJANGO 5')

def tuesday(request):
    return HttpResponse('Пройти как минимум два блока в курсе по DJANGO 5')
