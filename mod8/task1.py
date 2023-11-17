class Transport:
    def __init__(self, coordinates, speed, brand, year, number):
        self.coordinates = coordinates
        self.speed = speed
        self.brand = brand
        self.year = year
        self.number = number

    def __str__(self):
        """
           Представление всей информации для вывода в методе print()
        """
        return f'{self.__class__.__name__} [coordinates={self.coordinates}, speed={self.speed}, brand={self.brand}, year={self.year}, number={self.number}]'

    def isInArea(self, pos_x, pos_y, length, width) -> bool:
        """
        Присутствие транспортного средства в пределах заданной области
        pos_x, pos_y - координата левого верхнего угла области
        length, width - длина и ширина области
        """
        x, y = self.coordinates
        return pos_x <= x <= pos_x + length and pos_y <= y <= pos_y + width


class Passenger:
    def __init__(self, passengers_capacity, number_of_passengers):
        self._passengers_capacity = passengers_capacity
        self._number_of_passengers = number_of_passengers

    @property
    def passengers_capacity(self):
        return self._passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        self._passengers_capacity = passengers_capacity

    @property
    def number_of_passengers(self):
        return self._number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        self._number_of_passengers = number_of_passengers


class Cargo:
    def __init__(self, carrying):
        self._carrying = carrying

    @property
    def carrying(self):
        return self._carrying

    @carrying.setter
    def carrying(self, carrying):
        self._carrying = carrying


class Plane(Transport):
    def __init__(self, coordinates, speed, brand, year, number, height):
        super().__init__(coordinates, speed, brand, year, number)
        self.height = height


class Auto(Transport):
    def __init__(self, coordinates, speed, brand, year, number):
        super().__init__(coordinates, speed, brand, year, number)


class Ship(Transport):
    def __init__(self, coordinates, speed, brand, year, number, port):
        super().__init__(coordinates, speed, brand, year, number)
        self.port = port


class Car(Auto):
    class Bus(Auto, Passenger):
        class CargoAuto(Auto, Cargo):
            pass


class Boat(Ship):
    class PassengerShip(Ship, Passenger):

        class CargoShip(Ship, Cargo):
            pass


class Seaplane(Plane, Ship):
    pass
