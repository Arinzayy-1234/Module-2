
from django.urls import path

from . import views



urlpatterns = [
    path ('', views.index, name = 'index'),
    path ('book_list/', views.book_list, name = 'book_list'),
    path ('hello/', views.hello_view.as_view(), name = 'hello')
    # Add more URL patterns as needed
    ]