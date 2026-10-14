from django.http import HttpResponse


def book_list(request):
    return HttpResponse("Список всех книг")


def book_detail(request, pk):
    return HttpResponse(f"Детали книги с ID {pk}")


def book_add(request):
    return HttpResponse("Добавление новой книги")


def book_filter(request, genre, year):
    return HttpResponse(f"Книги жанра {genre} за {year} год")
