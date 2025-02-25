from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from math import pi

def get_rectangle_area(request, width: int, height: int):
    area = width * height
    return HttpResponse(f'Площадь прямоугольника размером {width}x{height} = {area}')

def get_square_area(request, width: int):
    area = width ** 2
    return HttpResponse(f'Площадь квадрата размером {width}x{width} = {area}')

def get_circle_area(request, radius: int):
    area = 2 * pi * radius
    return HttpResponse(f'Площадь круга с радиусом {radius} = {area}')
