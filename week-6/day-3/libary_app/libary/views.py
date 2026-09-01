from django.shortcuts import render
books =[
    {'id': 1, 'title': 'welcome to django', 'author': 'KHDIJAH', 'year': 2026},
    {'id': 2, 'title': 'FASTAPI demystified', 'author': 'NADA ', 'year': 2026},
]

def book_list(request):
    return render(request, 'libary/book_list.html', {'books': books})

def book_detail(request, id):
    book =books[id-1]
    return render(request, 'libary/book_detail.html', {'book': book})
