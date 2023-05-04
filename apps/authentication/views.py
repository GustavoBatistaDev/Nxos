from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def register(request: HttpRequest) -> HttpResponse:
    return render(request, 'authentication/register.html')

def dash(request):
    return HttpResponse('vc ta logado')