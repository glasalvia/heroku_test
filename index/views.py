from django.shortcuts import render
from django.template import loader

from django.http import HttpResponse




def index(request):
    context = {
        "author": "glasalvia",
        }
    return render(request, "index.html", context)