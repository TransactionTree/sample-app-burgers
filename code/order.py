import requests
import json
from BurgersUnlimited import settings
from HMACAuth import HMACAuth


def doubleQ(dict):
    return (json.dumps(dict))
def createPayload(dict):
    eDict = {}
    quantity = {
        "unitOfMeasure": "EA",
        "unitOfMeasureLabel": "",
        "value": dict['qty'],
    }
    unitPrice = dict["price"]
    productId = {
        "type": "",
        "value": dict['item'],
    }
    eDict.update({"productId": productId})
    eDict.update({"quantity": quantity})
    eDict.update({"unitPrice": unitPrice})

    return eDict
def createOrder(rawCart,userInfo):

    cart = rawCart.get('userCart')
    results = []

    for dict in range(len(cart)):
        results.append(createPayload(cart[dict]))
    modified_results = doubleQ(results)

    customer={
        'email': userInfo.get('email'),
        'firstName': userInfo.get('first_Name'),
        'lastName"': userInfo.get('last_Name')
    }

    modified_customer = doubleQ(customer)
    payload = "{\"comments\":\"This is a test\",\"customer\":%s,\"orderLines\":%s}"%(modified_customer,modified_results)
    url = 'https://gateway-staging.ncrcloud.com/order/orders'
    res = requests.post(url, payload, auth=(HMACAuth(settings.LOCATIONS["Burgers Unlimited Southland"])))
    result = res.json()
    print(result)
    return result['id']


cart = [{'item': 'SmallFries', 'price': 9.00, 'qty': 2}, {'item': 'Tunaburger', 'price': 13.00, 'qty': 2},{'item': 'milkshake', 'price': 11.00, 'qty': 2}]
temp = {'userCart': [{'item': 'Small Fries', 'price': '1.00', 'qty': 4}, {'item': 'Chickenburger', 'price': '9.00', 'qty': 4}, {'item': 'Tunaburger', 'price': '11.00', 'qty': 4}]}

user = {'email':'tempemail@email.com',
        'first_name':'Testa',
        'last_name':'SuperTest'}


#print(createOrder(temp,user))

def getOrder(orderId):
    headers = {
        'content-type': 'application/json',
        'nep-organization': 'burgers-unlimited',
        'nep-correlation-id': '2020-0708',
    }
    url = 'https://gateway-staging.ncrcloud.com/order/3/orders/1/%s'%orderId
    res = requests.get(url, auth=(HMACAuth()), headers=headers)
    result = res.json()
    print(result)

def getOrders():
    url = 'https://gateway-staging.ncrcloud.com/order/3/orders/1/find?pageNumber=0&pageSize=10'

    payload = "{\"customerEmail\":\"test@ncr.com\",\"returnFullOrders\":true}"

    res = requests.post(url, payload, auth=(HMACAuth()))
    result = res.json()
    print(result)



'''
def doubleQ(dict):
    return (json.dumps(dict))
def createPayload(dict):
    eDict = {}
    quantity = {
        "unitOfMeasure": "EA",
        "unitOfMeasureLabel": "",
        "value": dict['qty'],
    }
    unitPrice = dict["price"]
    productId = {
        "type": "",
        "value": dict['item'],
    }
    eDict.update({"productId": productId})
    eDict.update({"quantity": quantity})
    eDict.update({"unitPrice": unitPrice})

    #print((eDict.get('unitPrice')))
    #print(eDict)
    return eDict
def createOrder(cart):

    results = []

    for dict in range(len(cart)):
        results.append(createPayload(cart[dict]))
    modified_results = doubleQ(results)

    customer={
        "email": "test@ncr.com",
        "firstName": "Testy",
        "lastName": "McTest Test"
    }

    modified_customer = doubleQ(customer)
    payload = "{\"comments\":\"This is a test4\",\"customer\":%s,\"orderLines\":%s}"%(modified_customer,modified_results)
    url = 'https://gateway-staging.ncrcloud.com/order/orders'
    res = requests.post(url, payload, auth=(HMACAuth(settings.LOCATIONS["Burgers Unlimited Southland"])))
    result = res.json()
    print(result)
    return result['id']


'''


#getOrders()
getOrder('13101291033401619317')