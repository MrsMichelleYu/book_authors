from django.shortcuts import render, redirect
from .models import Book
from .models import Author 

def index(request):
    context = {
        "all_books": Book.objects.all(),
    }
    return render(request, "books_authors_app/index.html", context)

def book_description(request, id):
    some_book = Book.objects.get(id=id)
    some_book_authors = some_book.authors.all()
    context = {
        "book": Book.objects.get(id=id),
        "all_authors": some_book_authors,
        "database_authors": Author.objects.all()
    }
    print(context)
    return render(request, "books_authors_app/book_description.html", context)

def add_book(request):
    if request.method == "POST":
        new_title = request.POST["title"]
        new_description = request.POST["description"]
        Book.objects.create(title=f"{new_title}", description=f"{new_description}")
        return redirect("/")

def add_author_id(request, id):
    if request.method == "POST":
        added_author = request.POST["to_add_author"]
        some_book = Book.objects.get(id=id)
        some_book.authors.add(added_author)
        return redirect(f"/books/{id}")

def authors(request):
    context = {
        "all_authors": Author.objects.all(),
    }
    return render(request, "books_authors_app/authors.html", context)

def add_author(request):
    if request.method == "POST":
        new_first_name = request.POST["first_name"]
        new_last_name = request.POST["last_name"]
        new_notes = request.POST["notes"]
        Author.objects.create(first_name=f"{new_first_name}", last_name=f"{new_last_name}", notes=f"{new_notes}")
        return redirect("/authors")

def author_description(request, id):
    some_author = Author.objects.get(id=id)
    some_author_books = some_author.books.all()
    context = {
        "author": Author.objects.get(id=id),
        "all_books": some_author_books,
        "database_books": Book.objects.all()
    }
    print(context)
    return render(request, "books_authors_app/author_description.html", context)

def add_book_id(request, id):
    if request.method == "POST":
        added_book = request.POST["to_add_book"]
        some_author = Author.objects.get(id=id)
        some_author.books.add(added_book)
        return redirect(f"/authors/{id}")
