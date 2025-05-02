from django.urls import path
from app.views import index, about, menu, book, menu_item

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('menu', menu, name='menu'),
    path('book', book, name='book'),
    path('item/<int:pk>', menu_item, name='menu_item'),
]