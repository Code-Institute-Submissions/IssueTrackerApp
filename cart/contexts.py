"""Context for storing cart info in sessions until user logs out"""
from django.shortcuts import get_object_or_404
from tickets.models import Ticket

def cart_contents(request):
    """Ensure that the cart contents are availible when rendering every page"""
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    for id, amount in cart.items():
        new_feature = get_object_or_404(Ticket, pk=id)
        total += amount
        cart_items.append({'id': id, 'amount': amount, 'new_feature': new_feature})
    return {'cart_items': cart_items, 'total': total}
