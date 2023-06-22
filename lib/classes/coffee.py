class Coffee:
    def __init__(self, name):
        self.name = name
        self._orders = []
        #this should have an array of order and an array for customer
        self._customers = []

    @property
    def name (self):
        return self._name    
    
    @name.setter
    def name (self, name):
        if isinstance (name, str) and not hasattr(self, 'name'):
            self._name = name
        else:
            raise Exception
        
    def orders(self, new_order=None):
        from classes.order import Order
        if new_order and isinstance(new_order, Order):
            self._orders.append(new_order)
        return self._orders
    
    def customers(self, new_customer=None):
        from classes.customer import Customer
        if new_customer and isinstance(new_customer, Customer) and new_customer not in self._customers:
            self._customers.append(new_customer)
        return self._customers
    
    def num_orders(self):
        return len(self._orders) #check this
    
    def average_price(self):
        #we need to get the prices of all the orders
        #get the sum of them
        #divide by the number of orders AKA len()
        #[for in if]
        return sum (
            [order.price for order in self._orders if self._name == order.coffee.name]) / len(self._orders)
        