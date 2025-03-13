from http.client import responses

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from datetime import date as dt

signs_zodiacs = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).'
}

elements_zodiac = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}

signs_zodiac_by_day = {
    'aries': (dt(4, 3, 21), dt(4, 4, 20)),
    'taurus': (dt(4, 4, 21), dt(4, 5, 21)),
    'gemini': (dt(4, 5, 22), dt(4, 6, 21)),
    'cancer': (dt(4, 6, 22), dt(4, 7, 22)),
    'leo': (dt(4, 7, 23), dt(4, 8, 21)),
    'virgo': (dt(4, 8, 22), dt(4, 9, 23)),
    'libra': (dt(4, 9, 24), dt(4, 10, 23)),
    'scorpio': (dt(4, 10, 24), dt(4, 11, 22)),
    'sagittarius': (dt(4, 11, 23), dt(4, 12, 22)),
    'capricorn': (dt(3, 12, 23), dt(4, 1, 20)),
    'aquarius': (dt(4, 1, 21), dt(4, 2, 19)),
    'pisces': (dt(4, 2, 20), dt(4, 3, 20))
}


def index(request):
    """Главная страница со знаками зодиака"""
    signs = list(signs_zodiacs)
    data = {
        'signs': signs_zodiacs,
    }
    return render(request, 'horoscope/index.html', context=data)


def get_element_page(request):
    """Страница со стихиями"""
    elements = list(elements_zodiac)
    data = {
        'elements': elements,
    }
    return render(request, 'horoscope/types.html', context=data)

    # li_elements = ''
    # for element in elements:
    #     redirect_url = reverse('get_signs_about_elements', args=(element,))
    #     li_elements += f'<li><a href={redirect_url}>{element.title()}</a></li>'
    #
    # response = f"""
    # <ul>
    #     {li_elements}
    # </ul>
    # """
    # return HttpResponse(response)


def get_signs_about_elements(request, element):
    """Получение знака зодиака из стихии"""
    # if element not in elements_zodiac:
    #     return HttpResponseNotFound(f'Такой стихии не существует - {element}')
    #
    # li_elements = ''
    # for sign in elements_zodiac[element]:
    #     redirect_url = reverse('name_zodiac', args=(sign,))
    #     li_elements += f'<li><a href={redirect_url}>{sign.title()}</a></li>'
    #
    # response = f"""
    #     <ul>
    #         {li_elements}
    #     </ul>
    #     """
    data ={
        'signs': elements_zodiac[element],
    }
    return render(request, 'horoscope/types_signs.html', context=data)
    # return HttpResponse(response)



def get_info_about_sign_zodiac_by_name(request, sign_zodiac: str):
    """Получение информации о знаке зодиака по имени"""
    description = signs_zodiacs.get(sign_zodiac, None)
    data = {
        'description_zodiac': description,
        'incorrect_sign_zodiac': sign_zodiac,
        'sign_for_title': sign_zodiac,
        'zodiacs': signs_zodiacs,
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)


def get_info_about_sign_zodiac_by_num(request, sign_zodiac: int):
    """Получение информации о знаке зодиака по номеру"""
    signs = list(signs_zodiacs)
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
                return HttpResponse(signs_zodiacs[sign])
        # return HttpResponseRedirect(redirect_url)

    except ValueError:
        return HttpResponseNotFound('Введен не верный месяц или день!')
