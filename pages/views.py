from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices, bedroom_choices, county_choices

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'county_choices': county_choices,
    }

    return render(request, 'pages/index.html', context)


def about(request):

    realtors = Realtor.objects.order_by('-hire_date')

    mvp = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp': mvp
    }
    return render(request, 'pages/about.html', context)