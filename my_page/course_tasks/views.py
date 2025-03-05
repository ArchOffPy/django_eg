from django.shortcuts import render

def actors(request):
    data = {
        'year_born': 1964,
        'city_born': "Бейрут",
        'movie_name': "На гребне Волны"
    }
    return render(request, 'course_tasks/actors.html', context=data)


def get_guinness_world_records(request):
    date = {
        'power': 'Narve Laeret',
        'bar_name': 'Bob`s BBQ & Grill',
        'count_needle': 1790
    }
    return render(request, 'course_tasks/guinnessworldrecords.html', context=date )
