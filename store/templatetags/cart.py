from django import template


register = template.Library()
# this below filter is to show the product is in cart if cart it will pass true else false
# using this true or false we can show when stat is true '+' '-' in the front end show false when stat false
@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    keys = cart.keys()
    for id in keys:
        #print(id, type(id))
        #print(product.id, type(product.id))
        if int(id) == product.id:
            return True
    return False

@register.filter(name='cart_quantity')
def cart_quantity(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0

    #print(key)
    #print(product, cart)
    #return True
