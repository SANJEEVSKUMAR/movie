from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def movie(request):
    return render(request, "akhil.html")


def movie1(request):
    return render(request, "amal.html")
