
class Order:
    all=[]

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
#brining in coffee.py
        coffee.orders(self)
        coffee.customers(customer)
#bringing in customer.py
        customer.orders(self)
        customer.coffees(coffee)
        
        Order.all.append(self)


@property
def price (self):
    return self._price

@price.setter
def price (self, price):
    if 1 <= len(price) <= 10:
        self._price = price
    else:
        raise Exception
    
@property
def coffee (self):
    return self._coffee

@ coffee.setter
def coffee (self, name):
    if isinstance(name,str):
        self._name = name
    else:
        raise Exception