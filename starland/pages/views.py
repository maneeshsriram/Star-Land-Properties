from django.shortcuts import render

from listings.models import Listing
from realtors.models import Realtor


def index(request):
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]
    data = {
        'listings': listings
    }
    return render(request, 'pages/index.html', data)


def about(request):
    realtors = Realtor.objects.order_by('-hire_date')
    mvp = Realtor.objects.all().filter(is_mvp=True)
    data = {
        'realtors': realtors,
        'mvp': mvp
    }
    return render(request, 'pages/about.html', data)
