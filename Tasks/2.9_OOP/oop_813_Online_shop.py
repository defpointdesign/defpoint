
class Shop():
    '''Represents online shop '''
    def __init__(self, shop_name, store_type, number_of_units):
        self.name = shop_name
        self.type = store_type
        self.numb = number_of_units
    def describe_shop(self):
        print(self.name)
        print(self.type)
        print(self.numb)

    def number_of_units (self):
        self.numb = input('Paste new numbers of unit: ')
    def open_shop(self):
        print ('Shop Is Open')

class Discount(Shop):
    def __init__(self, shop_name, store_type, number_of_units, discount_products):
        Shop.__init__(self, shop_name, store_type, number_of_units)
        self.discount = discount_products

    def get_discount_products(self):
        print(self.discount)



store = Shop('Vizyt','Gastronom', 20000)
store.describe_shop()
store.number_of_units()
store.open_shop()

store_discount = Discount('Vizyt','Gastronom', 20000, 'motherboards')
store_discount.get_discount_products()

