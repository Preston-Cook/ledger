class Inventory:
    def __init__(self, new_id, new_name, new_stock, new_price):
        self.__id = new_id
        self.__name = new_name
        self.__stock = new_stock
        self.__price = new_price
    
    # Getters and Setters
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_stock(self):
        return self.__stock
    
    def get_price(self):
        return self.__price
    
    # Restock if new stock positive
    def restock(self, new_stock):
        if new_stock > 0:
            self.__stock += new_stock
            return True
        return False
    
    # Check purchase can be done
    def purchase(self, purchase_qty):
        if self.__stock >= purchase_qty:
            self.__stock -= purchase_qty
            return True
        return False
    
    def __str__(self):
        return f'{self.__id}{self.__name:>25}{self.__price:>10}{self.__stock:>10}'