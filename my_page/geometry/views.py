from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
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

# def get_shape_area(request, **kwargs):
#     if not len(kwargs):
#         return HttpResponseNotFound(f'Заданы неверные параметры: {kwargs}')
#     if 'radius' in kwargs:
#         return HttpResponseRedirect(f'/calculate_geometry/circle/{kwargs["radius"]}')
#     if 'width' in kwargs and 'height' in kwargs:
#         return HttpResponseRedirect(f'/calculate_geometry/rectangle/{kwargs["width"]}/{kwargs["height"]}')
#     if 'width' in kwargs:
#         return HttpResponseRedirect(f'/calculate_geometry/square/{kwargs["width"]}')

def get_shape_area(request, width=None, height=None, radius=None):
    url = 'calculate_geometry'
    if radius is not None:
        return HttpResponseRedirect(f'/{url}/circle/{radius}')
    if width is not None and height is not None:
        return HttpResponseRedirect(f'/{url}/rectangle/{width}/{height}')
    if width is not None:
        return HttpResponseRedirect(f'/{url}/square/{width}')