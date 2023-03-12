from .models import Cart, Tax
from menu.models import FoodItem

def get_cart_counter(request):
    cart_count = 0
    if request.user.is_authenticated:
        try:
            cart_items = Cart.objects.filter(user=request.user)
            if cart_items:
                for cart_item in cart_items:
                    cart_count += cart_item.quantity
            else:
                cart_count = 0
        except:
            cart_count = 0

    return dict(cart_count=cart_count)

def get_cart_amounts(request):
    subtotal = 0
    tax = 0
    grand_total = 0
    tax_dict = {}
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
        print('cart items:',cart_items)
        for item in cart_items:
            fooditem = FoodItem.objects.get(pk=item.fooditem.id)
            print(item,fooditem, fooditem.price)
            subtotal += (fooditem.price * item.quantity)
        
        get_tax = Tax.objects.filter(is_active=True)
        #print(get_tax)
        for i in get_tax:
            tax_type = i.tax_type
            tax_percentage = i.tax_percentage
            tax_amount = round((subtotal * tax_percentage)/100, 2)
            print(tax_type, tax_percentage, tax_amount)
            #{'CGST':{'9.00':'2.16'}} We are storing tax_type, tax_percentage and tax_amount into a dict called tax_dict
            tax_dict.update({tax_type:{str(tax_percentage) : tax_amount}})
        #print(tax_dict)
        # tax = 0
        # for key in tax_dict.values():
        #     for x in key.values():
        #         tax = tax+x

        tax = sum(x for key in tax_dict.values() for x in key.values())
        #print(tax)
        grand_total = subtotal + tax
    print(tax_dict)
    return dict(subtotal=subtotal, tax=tax, grand_total=grand_total, tax_dict=tax_dict)