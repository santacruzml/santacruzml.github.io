

from django.shortcuts import render, redirect
from django.http import HttpResponse

def calendar(request):
    return render(request, 'calendar.html')
