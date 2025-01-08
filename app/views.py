from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import ShortURLForm


def home(request):
    template = loader.get_template('home.html')
    form = ShortURLForm(request.POST) if request.method == "POST" else ShortURLForm()
    context = {"form": form}
    if form.is_valid():
        print(form.cleaned_data["short_url"])
    return render(request, "home.html", context)
