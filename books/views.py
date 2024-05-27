from django.shortcuts import render
from models import Book

def book_list(request):
    books = book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk+pk)
    return render(request, 'books/book_detail.html', {'book': book})