from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Listing

# Create your views here.


def listings(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)

    data = {
        'listings': page_listings
    }
    return render(request, 'listings/listings.html', data)


def listing(request, id):
    listing = get_object_or_404(Listing, pk=id)
    data = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', data)


def search(request):
    query_list = Listing.objects.order_by('-list_date')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_list = query_list.filter(description__icontains=keywords)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            query_list = query_list.filter(city__iexact=city)

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            query_list = query_list.filter(state__iexact=state)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            query_list = query_list.filter(bedrooms__lte=bedrooms)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            query_list = query_list.filter(price__lte=price)

    data = {
        'querylist': query_list,
        'values': request.GET
    }

    return render(request, 'listings/search.html', data)
