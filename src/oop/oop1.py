# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
 
class Vehicle:
  pass
  # def __init__(self, name, transportation_mode):
  #   self.name = name
  #   self.transportation_mode = transportation_mode

  # def __str__(self):
  #   return f'{self.name} moves on ${self.transportation_mode}'

class GroundVehicle(Vehicle):
  pass
  # def __init__(self, name, transportation_mode, num_wheels, num_seats):
    # super().__init__(name, transportation_mode)
    # # self.name = name
    # # self.transportation_mode= transportation_mode
    # self.num_wheels = num_wheels
    # self.num_seats = num_seats

class Car(GroundVehicle):
  pass
  # def __init__(self, name, transportation_mode, num_wheels, num_seats, make, model):
  #   super().__init__(name, transportation_mode, num_wheels, num_seats)
  #   # self.name = name
  #   # self.transportation_mode= transportation_mode
  #   self.num_wheels = num_wheels
  #   self.num_seats = num_seats
  #   self.make = make
  #   self.model = model


class Motorcycle(GroundVehicle):
  pass
  # def __init__(self, name, transportation_mode, num_wheels, num_seats, make, model):
  #   super().__init__(name, transportation_mode, num_wheels, num_seats)
  #   # self.name = name
  #   # self.transportation_mode= transportation_mode
  #   self.num_wheels = num_wheels
  #   self.num_seats = num_seats
  #   self.make = make
  #   self.model = model

class FlightVehicle(Vehicle):
  pass
  # def __init__(self, name, transportation_mode, num_wheels, num_seats):
  #   super().__init__(name, transportation_mode)
  #   # self.name = name
  #   # self.transportation_mode= transportation_mode
  #   self.num_wheels = num_wheels
  #   self.num_seats = num_seats

class Airplane(FlightVehicle):
  pass
  # def __init__(self, name, transportation_mode, num_wheels, num_seats, make, model):
  #   super().__init__(name, transportation_mode, num_wheels, num_seats)
  #   # self.name = name
  #   # self.transportation_mode= transportation_mode
  #   self.num_wheels = num_wheels
  #   self.num_seats = num_seats


class Starship(FlightVehicle):
  pass
  # def __init__(self, name, transportation_mode, num_seats):
  #   super().__init__(name, transportation_mode)
  #   # self.name = name
  #   # self.transportation_mode= transportation_mode
  #   self.num_seats = num_seats


# car_honda = GroundVehicle("car", "land", "4", "5")
# honda_accord = Car("Honda Accord", "land", "4", "5", "honda", "accord")
# motorcycle_harley = Motorcycle("Harley Davidson", "land", "2", "2", "harley", "roadster")
# airplane_vehicle = FlightVehicle("airplane", "air", "6", "250" )
# titanic_ship = Starship("ship", "sea","1500")


# print(car_honda.name)
# print(car_honda.transportation_mode)
# print(honda_accord.make)
# print(motorcycle_harley.make)
# print (airplane_vehicle.num_seats)
