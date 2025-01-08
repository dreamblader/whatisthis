from django.shortcuts import render
from django.template import loader
from .forms import ShortURLForm
from . import services


def home(request):
    form = ShortURLForm(request.POST) if request.method == "POST" else ShortURLForm()
    result = None
    if form.is_valid():
        result = services.getURL(form.cleaned_data["short_url"])
    
    context = {"form": form, "result":result}
    
    return render(request, "home.html", context)