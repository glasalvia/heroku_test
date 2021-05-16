from django.shortcuts import render

# Create your views here.
def login(request):
    context = {
        "author": "glasalvia",
        }
    return render(request, "login.html", context)