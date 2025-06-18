"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# urls.py

from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('add-author/', views.add_author, name='add_author'),
    path('add-book/', views.add_book, name='add_book'),
    path('add-borrow/', views.add_borrow_record, name='add_borrow_record'),
    path('authors/', views.list_authors, name='list_authors'),
    path('books/', views.list_books, name='list_books'),
    path('borrows/', views.list_borrow_records, name='list_borrow_records'),
]
