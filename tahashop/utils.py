from .models import *
import json


def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
    print('cart:', cart)
    items = []
    order = {'get_cart_items': 0, 'get_cart_total': 0, 'shipping': False}
    cartItem = order['get_cart_items']
        
    try:
        for i in cart:
            cartItem += cart[i]['quantity']
            
            product = Product.objects.get(id=i)
            total = (product.price * cart[i]['quantity'])
            
            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]['quantity']
            
            item = {
                'product':{
                    'id' : product.id,
                    'name' : product.name,
                    'price' : product.price,
                    'imageURL' : product.imageURL,
                },
                'quantity' : cart[i]['quantity'],
                'get_total' : total
                }
            items.append(item)
            
            if product.digital == False:
                order['shipping'] = True
    except:
        pass
    return {'cartItem' : cartItem, 'order' : order, 'items' : items}


def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItem = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItem = cookieData['cartItem']
        order = cookieData['order']
        items = cookieData['items']
    return {'cartItem' : cartItem, 'order' : order, 'items' : items}