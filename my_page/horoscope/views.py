from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

signs_zodiac = {
    'aries': 'Знак зодиака ОВЕН',
    'taurus': 'Знак зодиака ТЕЛЕЦ',
    'gemini': 'Знак зодиака БЛИЗНЕЦЫ',
    'cancer': 'Знак зодиака РАК',
    'leo': 'Знак зодиака ЛЕВ',
    'virgo': 'Знак зодиака ДЕВА',
    'libra': 'Знак зодиака ВЕСЫ',
    'scorpio': 'Знак зодиака СКОРПИОН',
    'sagittarius': 'Знак зодиака СТРЕЛЕЦ',
    'capricorn': 'Знак зодиака КОЗЕРОГ',
    'aquarius': 'Знак зодиака ВОДОЛЕЙ',
    'pisces': 'Знак зодиака РЫБЫ'
}


class Fire():
    pass


class Earth():
    pass


class Air():
    pass


class Water():
    pass


def index(request):
    signs = list(signs_zodiac)

    elements = ''
    for sign in signs:
        redirect_url = reverse('sign_zodiac', args=(sign,))
        elements += f'<li><a href={redirect_url}>{sign.title()}</a></li>'

    response = f"""
    <ul>
        {elements}
    <ul>
    """
    return  HttpResponse(response)

def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = signs_zodiac.get(sign_zodiac, None)
    if description:
        return HttpResponse(description)
    return HttpResponseNotFound(f'Такого знака не существует - {sign_zodiac}')


def get_info_about_sign_zodiac_by_num(request, sign_zodiac: int):
    signs = list(signs_zodiac)
    if 0 < sign_zodiac > len(signs):
        return HttpResponseNotFound(f'Не верный порядковый номер знака зодиака - {sign_zodiac}')
    sign = signs[sign_zodiac - 1]
    redirect_url = reverse('sign_zodiac', args=(sign,))
    return HttpResponseRedirect(redirect_url)
