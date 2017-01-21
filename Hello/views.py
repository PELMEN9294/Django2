from django.http import HttpResponse, Http404
from django.shortcuts import render
import datetime
from books.models import Book

def hello(request):
    re = request.META['REMOTE_ADDR']
    return HttpResponse(re)
    #return render(request, 'Base.html')

def current_datetime(request):
    now = datetime.datetime.now()

    return render(request, 'current_time.html', {'current_date': now})

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()

    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)

    return render(request, 'hours_ahead.html', {'hour_offset': offset, 'next_time': dt})


def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append("Enter a search term")
        elif len(q) > 20:
            errors.append("Please enter at most 20 characters.")
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_result.html', {'books': books, 'query': q})

    return render(request, 'search_form.html', {'error': errors})