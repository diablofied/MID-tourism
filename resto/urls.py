from django.urls import path
from resto.views import *
app_name = 'resto'

urlpatterns = [
    path('', show_restaurant, name='show_restaurant'),
    path('create_resto/', create_restaurant, name = 'create_resto'),
    path('show_restaurant_json/', show_restaurant_json, name = 'show_restaurant_json'),
    path('delete_restaurant/<int:id>', delete_restaurant, name='delete_restaurant'),
]