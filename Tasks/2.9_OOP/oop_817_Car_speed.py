class Car:
    def __init__(self, car_company, car_model, car_year, car_speed):
        self.company = car_company
        self.model = car_model
        self.year = car_year
        self.speed = car_speed
        print('Characteristics of the car:')
        print( self.company, self.model,  self.year)
    def get_speed(self):
        print ('Current speed:', self.speed)
    def accelerate(self):
        self.speed += 5
        Car.speed = self.speed
        print('Current speed:', Car.speed)
    def brake (self):
        Car.speed = self.speed
        self.speed -= 5
        print('Current speed:', Car.speed)

volvo_v50 = Car('Volvo', 'V50', 2010, 0)
print('Car accelerates:')
volvo_v50.accelerate()
volvo_v50.accelerate()
volvo_v50.accelerate()
volvo_v50.accelerate()
volvo_v50.accelerate()
print('Car slows down:')
volvo_v50.brake()
volvo_v50.brake()
volvo_v50.brake()
volvo_v50.brake()
volvo_v50.brake()
volvo_v50.get_speed()
print('Car stopped')
