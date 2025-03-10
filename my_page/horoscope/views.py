from http.client import responses

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from datetime import date as dt
from dataclasses import dataclass
# from django.template.loader import render_to_string

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

elements_zodiac = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}


signs_zodiac_by_day = {
    'aries': (dt(4,3,21), dt(4, 4, 20)),
    'taurus': (dt(4,4,21), dt(4, 5, 21)),
    'gemini': (dt(4,5,22), dt(4, 6, 21)),
    'cancer': (dt(4,6,22), dt(4, 7, 22)),
    'leo': (dt(4,7,23), dt(4, 8, 21)),
    'virgo': (dt(4,8,22), dt(4, 9, 23)),
    'libra': (dt(4,9,24), dt(4, 10, 23)),
    'scorpio': (dt(4,10,24), dt(4, 11, 22)),
    'sagittarius': (dt(4,11,23), dt(4, 12, 22)),
    'capricorn': (dt(3,12,23), dt(4, 1, 20)),
    'aquarius': (dt(4,1,21), dt(4, 2, 19)),
    'pisces': (dt(4,2,20), dt(4, 3, 20))
}

def index(request):
    """Главная страница со знаками зодиака"""
    signs = list(signs_zodiac)

    elements = ''
    for sign in signs:
        redirect_url = reverse('name_zodiac', args=(sign,))
        elements += f'<li><a href={redirect_url}>{sign.title()}</a></li>'

    response = f"""
    <ul>
        {elements}
    <ul>
    """
    return HttpResponse(response)


def get_element_page(request):
    """Страница со стихиями"""
    elements = list(elements_zodiac)

    li_elements = ''
    for element in elements:
        redirect_url = reverse('get_signs_about_elements', args=(element,))
        li_elements += f'<li><a href={redirect_url}>{element.title()}</a></li>'

    response = f"""
    <ul>
        {li_elements}
    </ul>
    """
    return HttpResponse(response)


def get_signs_about_elements(request, element):
    """Получение знака зодиака из стихии"""
    if element not in elements_zodiac:
        return HttpResponseNotFound(f'Такой стихии не существует - {element}')

    li_elements = ''
    for sign in elements_zodiac[element]:
        redirect_url = reverse('name_zodiac', args=(sign,))
        li_elements += f'<li><a href={redirect_url}>{sign.title()}</a></li>'

    response = f"""
        <ul>
            {li_elements}
        </ul>
        """
    return HttpResponse(response)

@dataclass
class AboutMe:
    my_name: str
    my_age: int

    def __str__(self):
        return f'Мое имя - {self.my_name}, мой возраст - {self.my_age}'

def get_info_about_sign_zodiac(request, sign_zodiac: str):
    """Получение информации о знаке зодиака по имени"""
    # response = render_to_string('week_days/greeting.html')
    # return HttpResponseNotFound(f'Такого знака не существует - {sign_zodiac}')
    description = signs_zodiac.get(sign_zodiac, None)
    person = AboutMe('Vitaliy', 34)
    data = {
        'description_zodiac': description,
        'incorrect_sign_zodiac': sign_zodiac,
        'sign_for_title': sign_zodiac,
        'my_int': 123,
        'my_float': 3.14,
        'my_list': [1, 2, 3],
        'my_tuple': (1, 2, 3),
        'my_dict': {'name': 'Vitaly', 'age': 34},
        'my_class': person
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)


def get_info_about_sign_zodiac_by_num(request, sign_zodiac: int):
    """Получение информации о знаке зодиака по номеру"""
    signs = list(signs_zodiac)
    if 0 < sign_zodiac > len(signs):
        return HttpResponseNotFound(f'Не верный порядковый номер знака зодиака - {sign_zodiac}')
    sign = signs[sign_zodiac - 1]
    redirect_url = reverse('name_zodiac', args=(sign,))
    return HttpResponseRedirect(redirect_url)

def sign_by_day(request, month: int, day: int):
    """Получение информации о знаке зодиака по месяцу и дню месяца"""
    try:
        request_date = dt(4, month, day)
        redirect_url = ''
        for sign, date in signs_zodiac_by_day.items():
            if date[0] <= request_date <= date[1]:
                redirect_url = reverse('name_zodiac', args=(sign,))
                return HttpResponse(signs_zodiac[sign])
        # return HttpResponseRedirect(redirect_url)

    except ValueError:
        return HttpResponseNotFound('Введен не верный месяц или день!')