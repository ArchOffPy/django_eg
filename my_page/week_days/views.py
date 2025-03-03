from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

tasks_day = {
    'monday': 'Понедельник. Начать изучать DJANGO 5',
    'tuesday': 'Вторник. Пройти как минимум два блока в курсе по DJANGO 5',
    'wednesday': 'Среда. Выполнить задания блока и сделать коммит',
    'thursday': 'Четверг. Параллельно с ДЖАНГО начать изучать SQL',
    'friday': 'Пятница. Выполнить на отлично задания из блока',
    'saturday': 'Суббота. Выспаться, и поработать на выполнением заданий по Джанго',
    'sunday': 'Воскресенье. Повторить все действия по проейденому материалу за неделю',
}

def index(request):
    """Главная страница со днями недели"""
    days = list(tasks_day)

    elements = ''
    for day in days:
        redirect_url = reverse('days_by_name', args=(day,))
        elements += f'<li><a href={redirect_url}>{day.title()}</a></li>'

    response = f"""
    <ul>
        {elements}
    <ul>
    """
    return HttpResponse(response)


def get_task_from_day(request, choice_day: str):
    # description = tasks_day.get(choice_day, None)
    #
    # if description:
    #     return HttpResponse(description)
    #
    # return HttpResponseNotFound(f'Такого дня не существует: {choice_day}')
    return render(request, 'week_days/greeting.html')


def get_task_from_day_by_num(request, choice_day: int):
    tasks_day_keys = list(tasks_day)

    if 0 < choice_day > 7:
        return HttpResponseNotFound(f'Дня с номером "{choice_day}" не существует')

    day_by_num = tasks_day_keys[choice_day - 1]
    redirect_url = reverse('days_by_name', args=(day_by_num,))
    return HttpResponseRedirect(redirect_url)