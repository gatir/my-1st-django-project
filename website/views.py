from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse


def index_view(request):
    return HttpResponse('<h1>home page')


def contact_view(request):
    return HttpResponse('<h1>contact us')


def about_view(request):
    return HttpResponse('<h1>about us')
