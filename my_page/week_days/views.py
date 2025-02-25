from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

tasks_day = {
    'monday': 'Начать изучать DJANGO 5',
    'tuesday': 'Пройти как минимум два блока в курсе по DJANGO 5',
    'wednesday': 'Выполнить задания блока и сделать коммит',
    'thursday': 'Параллельно с ДЖАНГО начать изучать SQL',
    'friday': 'Выполнить на отлично задания из блока',
    'saturday': 'Выспаться, и поработать на выполнением заданий по Джанго',
    'sunday': 'Повторить все действия по проейденому материалу за неделю',
}


def get_task_from_day(request, choice_day):
    description = tasks_day.get(choice_day, None)
    if description:
        return HttpResponse(description)
    return HttpResponseNotFound(f'Не найден день: {choice_day}')
