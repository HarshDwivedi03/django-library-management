from django.shortcuts import render, redirect
from .forms import AuthorForm, BookForm, BorrowRecordForm
from .models import Author, Book, BorrowRecord
from django.core.paginator import Paginator

def home(request):
    return render(request, 'home.html')

def add_author(request):
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_authors')
    return render(request, 'add_author.html', {'form': form})

def add_book(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_books')
    return render(request, 'add_book.html', {'form': form})

def add_borrow_record(request):
    form = BorrowRecordForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_borrow_records')
    return render(request, 'add_borrow_record.html', {'form': form})

def list_authors(request):
    authors = Author.objects.all()
    paginator = Paginator(authors, 5)
    page = request.GET.get('page')
    authors_paginated = paginator.get_page(page)
    return render(request, 'list_authors.html', {'authors': authors_paginated})

def list_books(request):
    books = Book.objects.all()
    paginator = Paginator(books, 5)
    page = request.GET.get('page')
    books_paginated = paginator.get_page(page)
    return render(request, 'list_books.html', {'books': books_paginated})

def list_borrow_records(request):
    records = BorrowRecord.objects.all()
    paginator = Paginator(records, 5)
    page = request.GET.get('page')
    records_paginated = paginator.get_page(page)
    return render(request, 'list_borrow_records.html', {'records': records_paginated})
