from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


signs_zodiac = {
    'aries': 'Знак зодиака ОВЕН',
    'taurus': 'Знак зодиака ТЕЛЕЦ',
    'gemini': 'БЛИЗНЕЦЫ',
    'cancer': 'РАК',
    'leo': 'Знак зодиака ЛЕВ',
    'virgo': 'Знак зодиака ДЕВА',
    'libra': 'Знак зодиака ВЕСЫ',
    'scorpio': 'Знак зодиака СКОРПИОН',
    'sagittarius': 'Знак зодиака СТРЕЛЕЦ',
    'capricorn': 'Знак зодиака КОЗЕРОГ',
    'aquarius': 'Знак зодиака ВОДОЛЕЙ',
    'pisces': 'Знак зодиака РЫБЫ'
}

def get_info_about_sign_zodiac(request, sign_zodiac):
    return HttpResponse(signs_zodiac.get(
        sign_zodiac,
        HttpResponseNotFound(f'Такого знака не существует - {sign_zodiac}')
    ))
