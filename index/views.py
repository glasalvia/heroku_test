from django.shortcuts import render

def index(request):
    context = {
        "author": "glasalvia",
        }
    return render(request, "index.html", context)