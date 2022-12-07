class TransactionItem:
    def __init__(self):
        pass

    # Getters and Setters
    def set_id(self, new_id):
        self.__id = new_id

    def get_id(self):
        return self.__id
    
    def set_name(self, new_name):
        self.__name = new_name
    
    def get_name(self):
        return self.__name
    
    def set_qty(self, new_qty):
        self.__quantity = new_qty
    
    def get_qty(self):
        return self.__quantity
    
    def set_price(self, new_price):
        self.__price = new_price
    
    def get_price(self):
        return self.__price
    
    # Returns total for transaction
    def calc_cost(self):
        return self.__price * self.__quantity
    
    # Utility for formatting dollars to account for negative sign
    @staticmethod
    def formatted_amount(amt):
        if amt < 0:
            return f'-${abs(amt):,.2f}'
        return f'${amt:,.2f}'

    def __str__(self):
        return f'{self.__id}{self.__name:>25}{self.__quantity:>10}{self.__price:>10}{self.formatted_amount(self.calc_cost()):>10}'