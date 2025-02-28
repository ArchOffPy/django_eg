from django.urls import path
from . import views as views

urlpatterns = [
    path('', views.index, name='index'),
    path('type', views.get_element_page, name='get_element_page'),
    path('type/<element>', views.get_signs_about_elements, name='get_signs_about_elements'),
    path('<int:sign_zodiac>', views.get_info_about_sign_zodiac_by_num, name='num_zodiac'),
    path('<str:sign_zodiac>', views.get_info_about_sign_zodiac, name='name_zodiac'),
    path('<int:month>/<int:day>', views.sign_by_day, name='sign_by_day'),
]



