from django.urls import path
from . import views as views

urlpatterns = [
    path('<choice_day>/', views.get_task_from_day),
]