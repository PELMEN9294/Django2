from django.http import HttpResponse, Http404
from django.shortcuts import render
import datetime

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