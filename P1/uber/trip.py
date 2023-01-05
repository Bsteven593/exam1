from car import Car 
from account_driver import Driver
from account_usser import User
from route import Route
from payment import Payment

class Trip(Car, Driver, User, Route, Payment):
    trip = int
    
    car = Car("", "", "", "", "")
    driver = Driver("", "", "", "", "","")
    user = User ("", "", "", "", "")
    route = Route ("", "", "", "")
    payment = Payment("", "", "")
    
    def __init__(self, idTrip, car, driver, user, route, payment):
        self.trip = idTrip
        self.car  = car 
        self.driver = driver
        self.user  = user
        self.route  = route
        self.payment = payment