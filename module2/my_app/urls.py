
from django.urls import path

from . import views



urlpatterns = [
    path ('', views.index, name = 'index'),
    path ('book_list/', views.book_list, name = 'book_list'),
    path ('hello/', views.hello_view.as_view(), name = 'hello'),
    path ('book/<int:pk>/', views.BookDetailView.as_view(), name = 'book_detail'),
    # The <int:pk> captures the primary key of the book and passes it to the view
    # as the 'pk' argument, which is used by the DetailView to retrieve the # specific book instance.
    # Add more URL patterns as needed
    path ('book/<int:pk>/', views.BookDetailView.as_view(), name = 'book_detail')
    ]