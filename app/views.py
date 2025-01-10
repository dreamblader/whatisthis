from django.shortcuts import render
from django.template import loader
from .forms import ShortURLForm
from django.conf import settings
from . import services


def home(request):
    form = ShortURLForm(request.POST) if request.method == "POST" else ShortURLForm()
    result = None
    error = False
    if form.is_valid():
        try:
            result = services.getURL(form.cleaned_data["short_url"])
        except Exception as error:
            if settings.DEBUG:
                print(error)
            error = True
    
    context = {"form": form, "result":result, "error":error}
    
    return render(request, "home.html", context)