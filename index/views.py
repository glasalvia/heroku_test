from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


@login_required(login_url='/accounts/login/')
def index(request):
    context = {
        "author": "glasalvia",
        }
    return render(request, "index.html", context)

@login_required(login_url='/accounts/login/')
def activarBotTelegram(request):
    print("Bot activado")
    return JsonResponse([{"status":"ok"}], safe=False)
