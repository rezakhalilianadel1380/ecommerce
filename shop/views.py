from django.shortcuts import render,HttpResponse



def homepage(request):
    return HttpResponse('hello world ')