from django.urls import path
from . import views as views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:sign_zodiac>', views.get_info_about_sign_zodiac_by_num),
    path('<str:sign_zodiac>', views.get_info_about_sign_zodiac, name='sign_zodiac'),
]