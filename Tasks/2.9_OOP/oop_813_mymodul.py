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