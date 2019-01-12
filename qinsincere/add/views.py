from django.shortcuts import render

def index(request):
    return HttpResponse("You're at the add index.")