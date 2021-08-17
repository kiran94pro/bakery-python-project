class Bakery_product:
    # constructor to set default values of product class property
    def __init__(self, name, note, packaging, value):
        self.name = name
        self.note = note
        self.packaging = packaging
        self.value = value

class User_interface:
    def __init__(self):
        self.menu = {}

    def create_item(self, bakeryproduct):
        note = input('Enter short notes on the item: ')
        packaging = input('Enter the state of package broken (or) unbroken: ').lower()
        if packaging not in ['broken', 'unbroken']:
            print(f"{packaging} is not either broken or unbroken. Please enter correct option")
            return False
        try:
            value = float(input('Enter the price of item: '))
        except ValueError:
            print("Please Enter the correct price")
            return False
        self.menu[bakeryproduct] = Bakery_product(bakeryproduct, note, packaging, value)
        return True

    def read_item(self, bakeryproduct):
        if bakeryproduct in self.menu:
            print(f'Name: {self.menu[bakeryproduct].name}')
            print(f'Short notes on item: {self.menu[bakeryproduct].note}')
            print(f'State of the package: {self.menu[bakeryproduct].packaging}')
            print(f'price: {self.menu[bakeryproduct].value}')
        else:
            print(f"Sorry, {bakeryproduct} is not present in the menu")

    def update_item(self, bakeryproduct, note, packaging, value):
        if bakeryproduct in self.menu:
            if note != '':
                self.menu[bakeryproduct].note = note
            if packaging != '':
                if packaging not in ['broken', 'unbroken']:
                    print(F"{packaging} is not either broken or unbroken. Please enter correct option")
                else:
                    self.menu[bakeryproduct].packaging = packaging
            if value != '':
                try:
                    float(value)
                    self.menu[bakeryproduct].value = value
                except ValueError:
                    print("Please Enter an Number")
        else:
            print(f"{bakeryproduct} is not in the menu")

    def delete_item(self, bakeryproduct):
        if bakeryproduct in self.menu:
            del self.menu[bakeryproduct]
        else:
            print(f"{bakeryproduct} is not in the menu")

    def exit(self):
        print("Thank you for checking our menu today.")

    def create_an_User_Interface(self):
        choice = 0
        create_an_item = 1
        read_an_item = 2
        update_an_item = 3
        delete_an_item = 4
        exit = 5

        while choice != exit:
            print('\n Welcome to the Bakerys Menu ')
            print('1) Add new item')
            print('2) Read about the item')
            print('3) Update an item')
            print('4) Delete an item')
            print('5) Exit\n')

            choice = int(input('Enter your option: '))

            if choice == create_an_item:
                name = input('Enter the name of new item: ')
                if self.create_item(name):
                    print(f'\n{name} is added\n')

            elif choice == read_an_item:
                bakeryproduct = input("\n Enter the item's name: \n")
                self.read_item(bakeryproduct)

            elif choice == update_an_item:
                bakeryproduct = input('Enter the name of updating item: ')
                if bakeryproduct in self.menu:
                    note = input('Enter updated short notes, else leave it empty: ')
                    packaging = input('Enter updated package status, else leave it empty: ').lower()
                    value = input('Enter updated price, else leave it empty: ')
                    self.update_item( bakeryproduct, note, packaging, value)
                    print(f'\n{ bakeryproduct} is updated\n')
                else:
                    print('the item is not found in the menu')
            elif choice == delete_an_item:
                bakeryproduct = input("\n Which item do you want to delete? \n")
                if bakeryproduct in self.menu:
                    self.delete_item(bakeryproduct)
                    print("Item is deleted")
                else:
                    print('item is not found in the menu')
            elif choice == exit:
                self.exit()

            else:
                print("Please enter the correct option")

interface = User_interface()
interface.create_an_User_Interface()