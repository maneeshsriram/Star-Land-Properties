from django.contrib import messages
from django.shortcuts import redirect
# from django.core.mail import send_mail

from .models import Contact


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
            user_id = request.user.id
            contacted = Contact.objects.all().filter(
                listing_id=listing_id, user_id=user_id)
            if contacted:
                messages.error(request, 'Message already sent')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email,
                          phone=phone, message=message, user_id=user_id, realtor_email=realtor_email)
        contact.save()

        # send_mail(
        #     'Start Land Properties',
        #     listing,
        #     'from@example.com',
        #     ['to@example.com'],
        #     fail_silently=False,
        # )

        messages.success(request, 'Message submitted!')
        return redirect('/listings/'+listing_id)
