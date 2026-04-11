from django.shortcuts import render
from django.http import HttpResponse
from .models import Sushi

# Create your views here.
def chirashizushi(request):
    return render(request, 'chirashizushi.html', {"nome": "Evandro"})

def tsurasuzusu(request):
    if(request.method == "POST"):
        post = {"chirashi": request.POST.get("chirashi"), "sushi": request.POST.get("sushi")}
        
        return render(request, "tsurasuzusu.html", post | {"nome": "Evandro"})
    else:
        return render(request, "tsurasuzusu.html", {"nome": "Evandro", "chirashi": 10, "sushi": "Chirashisushi"})
