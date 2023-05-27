from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .choices import price_choices, bedroom_choices, county_choices

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)
    
    context = {
        'listings': page_listings,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'county_choices': county_choices,
    }

    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    # display 404 page if id doesn't exist
    #listing_id is coming from the urls.py being passed through the url
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)

def search(request):

    context = {
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'county_choices': county_choices,
    }
    return render(request, 'listings/search.html', context)