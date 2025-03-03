from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from math import pi

def get_rectangle_area(request, width: int, height: int):
    # area = width * height
    # return HttpResponse(f'Площадь прямоугольника размером {width}x{height} = {area}')
    return render(request, 'geometry/rectangle.html')

def get_square_area(request, width: int):
    # area = width ** 2
    # return HttpResponse(f'Площадь квадрата размером {width}x{width} = {area}')
    return render(request, 'geometry/square.html')

def get_circle_area(request, radius: int):
    # area = 2 * pi * radius
    # return HttpResponse(f'Площадь круга с радиусом {radius} = {area}')
    return render(request, 'geometry/circle.html')

# def get_shape_area(request, **kwargs):
#     if not len(kwargs):
#         return HttpResponseNotFound(f'Заданы неверные параметры: {kwargs}')
#     if 'radius' in kwargs:
#         return HttpResponseRedirect(f'/calculate_geometry/circle/{kwargs["radius"]}')
#     if 'width' in kwargs and 'height' in kwargs:
#         return HttpResponseRedirect(f'/calculate_geometry/rectangle/{kwargs["width"]}/{kwargs["height"]}')
#     if 'width' in kwargs:
#         return HttpResponseRedirect(f'/calculate_geometry/square/{kwargs["width"]}')

# def get_shape_area(request, width=None, height=None, radius=None):
#     url = 'calculate_geometry'
#     if radius is not None:
#         return HttpResponseRedirect(f'/{url}/circle/{radius}')
#     if width is not None and height is not None:
#         return HttpResponseRedirect(f'/{url}/rectangle/{width}/{height}')
#     if width is not None:
#         return HttpResponseRedirect(f'/{url}/square/{width}')

def get_shape_area(request, width=None, height=None, radius=None):
    if radius is not None:
        redirect_url = reverse('circle', args=(radius,))
        return HttpResponseRedirect(redirect_url)
    if width is not None and height is not None:
        redirect_url = reverse('rectangle', args=(width, height))
        return HttpResponseRedirect(redirect_url)
    if width is not None:
        redirect_url = reverse('square', args=(width,))
        return HttpResponseRedirect(redirect_url)