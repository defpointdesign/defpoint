class SchoolClass:
    '''Represents school class pupil'''
    def __init__(self, class_name):
        self.name = class_name
        self.pupil_list = []

    def add_pupil(self, name, surname):
       self.pupil_list.append({ "name": name, "surname": surname})

    def show_pupils(self):
        for pupil in self.pupil_list:
            print(pupil['name'], pupil['surname'])

    def show_pupils_amount(self):
        print(len(self.pupil_list))

    def show_class_name(self):
        print(self.name)

hui = SchoolClass('9-B')

hui.show_class_name()
hui.add_pupil('vadim', 'oliinyk')
hui.add_pupil('yulia', 'raboshuk')

hui.show_pupils()

nineA = SchoolClass('9-A')

nineA.show_class_name()
nineA.add_pupil('roma', 'druz')
nineA.add_pupil('oleksiy', 'raboshuk')

nineA.show_pupils()


