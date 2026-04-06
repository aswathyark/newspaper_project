from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.utils import translation
from .models import News
from django.shortcuts import render

def index(request):
    articles = News.objects.all()
    return render(request, "index.html", {"articles": articles})

