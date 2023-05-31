from django.shortcuts import redirect
from django.contrib import messages
from .models import Contact

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        realtor_email = request.POST['realtor_email']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        
        contact = Contact(listing=listing, listing_id=listing_id, realtor_email=realtor_email, name=name, email=email, phone=phone,
                          message=message, user_id=user_id)
        contact.save()

        messages.success(request, 'Thanks! Your inquiry has been submitted, an agent will get back to you soon!')
        return redirect('/listings/'+listing_id)