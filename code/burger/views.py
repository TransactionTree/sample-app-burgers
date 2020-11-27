from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
import auxMethods
import catalogMaker
import order
import json
from django.views.decorators.cache import never_cache

HIGHLANDS = settings.LOCATIONS['Burgers Unlimited Highlands']
SOUTHLAND = settings.LOCATIONS['Burgers Unlimited Southland']
MIDTOWN = settings.LOCATIONS['Burgers Unlimited Midtown']
SHOPPINGCART = {}


def index(request):
    return render(request, 'index.html')


def findRestaurant(request):
    address = request.POST['address']
    radius = int(request.POST['radius'])

    coordinates = auxMethods.geoCodeAddress(address)

    if coordinates is None:
        return render(request, 'addressNotFound.html')

    results = auxMethods.findResturantsInRange(coordinates, radius)
    context = {'address': address, "radius": radius,
               'coordinates': coordinates, 'results': results}

    return render(request, 'findRestaurant.html', context)


def midtownMenu(request):
    try:
        items = catalogMaker.getStoreItems('BurgersUnlimitedMidtown')
        items_prices = catalogMaker.getAllPrices(items, MIDTOWN)
    except:
        return render(request, 'error.html')
    context = {'items': items_prices}

    return render(request, 'midtownMenu.html', context)


def southlandMenu(request):
    try:
        items = catalogMaker.getStoreItems('BurgersUnlimitedSouthland')
        items_prices = catalogMaker.getAllPrices(items, SOUTHLAND)
    except:
        return render(request, 'error.html')
    context = {'items': items_prices}

    return render(request, 'southlandMenu.html', context)


def highlandsMenu(request):
    try:
        items = catalogMaker.getStoreItems('BurgersUnlimitedHighlands')
        items_prices = catalogMaker.getAllPrices(items, HIGHLANDS)
    except:
        return render(request, 'error.html')
    context = {'items': items_prices}

    return render(request, 'highlandsMenu.html', context)


def payment(request):
    return render(request, 'payment.html')

@never_cache
def viewCart(request):
    return render(request, 'viewCart.html')


def confirmation(request):
    global SHOPPINGCART
    if request.user.is_authenticated and SHOPPINGCART['userCart'][0]['item'] != '0':
       user = {'email': request.user.email,
               'first_name': request.user.first_name,
               'last_name': request.user.last_name}
       orderId = order.createOrder(SHOPPINGCART,user)
       getOrder = order.getOrder(orderId)
       context = {'test':SHOPPINGCART,'orderId':orderId,'getOrder':getOrder}
       SHOPPINGCART = ''
       return render(request, 'confirmation.html',context)
    else:
        SHOPPINGCART = ''
        return render(request,'confirmation.html')

def shoppingCart(request):
    global SHOPPINGCART
    if request.method == 'POST':
        SHOPPINGCART = json.loads(request.body)
    return HttpResponse("Success")


def documentation(request):
    return render(request, 'documentation.html')
