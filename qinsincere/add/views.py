from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("You're at the add index.")