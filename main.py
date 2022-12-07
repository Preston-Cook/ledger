from inventory import Inventory
from transactionitem import TransactionItem
import sys

# Global variables to track inventory and transactions
inventory_list = []
transaction_list = []


def main():
    # Read in existing inventory from file
    process_inventory()

    while True:
        # Pretty print inventory to user
        print_inventory()

        # Get item id from user
        user_id = get_user_id()

        # User tries to exit program
        if user_id == '0':

            # Update inventory
            write_updated_inventory()

            # Pretty print transactions and exit with code 0
            print_invoice()
            sys.exit(0)
        else:
            # Get item qty from user
            get_user_quantity(user_id)


def process_inventory():
    global inventory_list

    # Loop over inventory file in increments of 4
    with open('inventory.txt') as f:
        lines = f.read().splitlines()
        for i in range(len(lines) // 4):
            entry = lines[i * 4: (i + 1) * 4]

            id, name, stock, price = entry[0], entry[1], float(entry[2]), float(entry[3])

            # Instantiate inventory object and append to global var
            inventory_obj = Inventory(id, name, stock, price)
            inventory_list.append(inventory_obj)


def print_inventory():
    global inventory_list

    # ljust headers and loop through inventory list
    print(f'ID{"Item":>26}{"Price":>10}{"Stock":>10}')
    for item in inventory_list:
        print(item)
    print('Enter 0 when finished')


def get_user_id():
    global inventory_list

    # map getter to collect ids
    id_lst = list(map(Inventory.get_id, inventory_list)) + ['0']

    # Prompt user for item id and validate input
    user_id = input('\nPlease enter the item ID you with to purchase/return: ')

    while user_id not in id_lst:
        print('Input was invalid.')
        user_id = input('\nPlease enter the item ID you with to purchase/return: ')

    return user_id


def get_user_quantity(user_id):
    global inventory_list

    # Filter objects to get objects with id and get stock
    item = list(filter(lambda x: x.get_id() == user_id, inventory_list))[0]
    stock = item.get_stock()

    # Prompt user for quantity and validate input
    user_quantity = float(input('\nPlease enter the desired quantity (negative quantity for return): '))

    while user_quantity == 0:
        print('Input was invalid')
        user_quantity = float(
            input('\nPlease enter the desired quantity (negative quantity for return): '))

    # Check if there is enough stock
    if user_quantity > 0 and user_quantity > stock:
        print('\nSorry we do not have enough stock\n')
        return

    # Instantiate TransactionItem and append to global var
    transac_item = TransactionItem()
    transac_item.set_id(item.get_id())
    transac_item.set_name(item.get_name())
    transac_item.set_price(item.get_price())
    transac_item.set_qty(user_quantity)

    transaction_list.append(transac_item)

    # Check for restock or purchase
    if user_quantity < 0:
        item.restock(abs(user_quantity))
        return

    if user_quantity > 0:
        item.purchase(user_quantity)
        return


def write_updated_inventory():
    global inventory_list

    # Loop through inventory global var and write attrs to file
    with open('UpdatedInventory.txt', 'w') as f:
        for item in inventory_list:
            f.write(
                f'{item.get_id()}\n{item.get_name()}\n{item.get_stock()}\n{item.get_price()}\n')


def print_invoice():
    global transaction_list
    
    # Tracker for transaction total
    grand_total = 0

    print(f'ID{"Item":>26}{"Qty":>10}{"Price":>10}{"Total":>10}')

    # Loop through transactions and add cost to total
    for transaction in transaction_list:
        print(transaction)
        grand_total += transaction.calc_cost()

    tax = 0

    # Call static method to format transaction and add tax if there
    print(f'\nPrice: {TransactionItem.formatted_amount(grand_total)}')
    if grand_total > 0:
        tax = grand_total * 0.085
        print(f'Tax: {TransactionItem.formatted_amount(tax)}')
    print(f'Total: {TransactionItem.formatted_amount(grand_total + tax)}')


if __name__ == '__main__':
    main()