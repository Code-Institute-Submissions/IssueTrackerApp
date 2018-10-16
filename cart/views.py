"""Views for cart"""
from django.shortcuts import render, redirect, reverse

def view_cart(request):
    """Render all cart contents"""
    return render(request, 'cart.html')

def add_to_cart(request, id):
    """Add new feature with amount to pay to cart"""
    amount = int(request.POST.get('amount'))
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, amount)
    request.session['cart'] = cart
    return redirect(reverse('tickets'))

def adjust_amount(request, id):
    """Adjust amount to pay"""
    amount = int(request.POST.get('amount'))
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, amount)
    cart[id] = amount
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
