"""View for checkout"""
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.utils import timezone
import stripe
from tickets.models import Ticket
from .models import NewFeatureUpvote
from .forms import MakePaymentForm

stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    """Checkout view"""
    if request.method == 'POST':
        payment_form = MakePaymentForm(request.POST)
        # If form is valid
        if payment_form.is_valid():
            cart = request.session.get('cart', {})
            total = 0
            new_feature_to_upvote = []
            # Add username and date and save order
            for id, amount in cart.items():
                new_feature = get_object_or_404(Ticket, pk=id)
                new_feature_to_upvote.append((new_feature, amount))
                total += amount
                new_feature_upvote = NewFeatureUpvote(username=request.user.username, amount=total, new_feature=new_feature, date=timezone.now())
                new_feature_upvote.save()
            # Try payment, fetch errors
            try:
                customer = stripe.Charge.create(
                    amount=int(total*100),
                    currency='EUR',
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                    )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            # If payment was successful
            if customer.paid:
                messages.error(request, "Your payment was successfull!")
                # Upvote payed features, add amount to payments
                for feature in new_feature_to_upvote:
                    ticket = Ticket.objects.get(pk=feature[0].pk)
                    ticket.votes.up(user_id=request.user.pk)
                    amount = feature[1]
                    ticket.payments += amount
                    ticket.save()
                request.session['cart'] = {}
                return redirect(reverse('tickets'))
            # If payment was not successful
            else:
                messages.error(request, "Payment was not successful!")
        # If form is not valid
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to make a payment with that card!")
    else:
        payment_form = MakePaymentForm

    return render(request, 'checkout.html', {'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})
