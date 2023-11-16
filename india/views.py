from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def sachin(request):
    return HttpResponse('sachin is a great player')

def msd(request):
    return HttpResponse('msd is the best player')