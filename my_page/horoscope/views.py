from django.shortcuts import render
from django.http import HttpResponse


def aries(request):
    return HttpResponse("Знак зодиака ОВЕН")

def taurus(request):
    return HttpResponse("Знак зодиака ТЕЛЕЦ")

def gemini(request):
    return HttpResponse("Знак зодиака БЛИЗНЕЦЫ")

def cancer(request):
    return HttpResponse("Знак зодиака РАК")

def leo(request):
    return HttpResponse("Знак зодиака ЛЕВ")

def virgo(request):
    return HttpResponse("Знак зодиака ДЕВА")

def libra(request):
    return HttpResponse("Знак зодиака ВЕСЫ")

def scorpio(request):
    return HttpResponse("Знак зодиака СКОРПИОН")

def sagittarius(request):
    return HttpResponse("Знак зодиака СТРЕЛЕЦ")

def capricorn(request):
    return HttpResponse("Знак зодиака КОЗЕРОГ")

def aquarius(request):
    return HttpResponse("Знак зодиака ВОДОЛЕЙ")

def pisces(request):
    return HttpResponse("Знак зодиака РЫБЫ")
