from django.urls import path
from . import views as views

urlpatterns = [
    path('<int:choice_day>', views.get_task_from_day_by_num),
    path('<str:choice_day>', views.get_task_from_day, name='days_by_name'),
]