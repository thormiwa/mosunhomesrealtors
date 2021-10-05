from django.shortcuts import render, get_object_or_404
from .models import Listings

# Create your views here.

def index(request):
    return render(request, 'blog/index.html', {})

def about(request):
    return render(request, 'blog/about.html', {})

def portfolio(request):
    listing = Listings.objects.all()
    return render(request = request, template_name='blog/portfolio.html', context={'listing':listing})

def detail(request, pk):
    listing = get_object_or_404(Listings, pk=pk)
    context={'listing':listing}
    return render(request,"blog/detail.html",context)

def contact(request):
    return render(request, 'blog/contact.html', {})