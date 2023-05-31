from django.shortcuts import redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail


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

        #check if user has existing inquiry

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, "You have made an inqury for this property")
                return redirect('/listings/'+listing_id)
        
        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone,
                          message=message, user_id=user_id)
        contact.save()
        
        #send email
        send_mail("Property inquiry",
                  "Inquiry for" + listing + 'find out more in the admin panel',
                  "c.martinroffey@gmail.com",
                  [realtor_email, 'c.martinroffey@gmail.com'],
                  fail_silently=False,)

        messages.success(request, 'Thanks! Your inquiry has been submitted, an agent will get back to you soon!')
        return redirect('/listings/'+listing_id)