
from django.shortcuts import render, redirect
from apps.store.models import Product

def cart_detail(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0
    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(id=product_id)
            items.append({'product': product, 'quantity': quantity})
            total += product.price * quantity
        except Product.DoesNotExist:
            pass
    return render(request, 'cart/cart_detail.html', {'items': items, 'total': total})

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    return redirect('store_home')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart.pop(str(product_id), None)
    request.session['cart'] = cart
    return redirect('cart_detail')
