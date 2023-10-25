from enum import Enum


class Rooms(Enum):
    one = '1'
    two = '2'
    three = '3'
    four = '4'
    five = '5'
    six = '6'
    seven = '7'
    eight = '8'
    nine = '9'
    ten = '10'
    more = 'more than 10'

    @classmethod
    def choices(cls):
        return [(item.name, item.value) for item in cls]


class Development(Enum):
    house = 'Detached house'
    block = 'Block'
    tenement = 'Tenement house'
    rowhouse = 'Rowhouse'
    semi = 'Semi-detached house'
    loft = 'Loft'
    apartment = 'Apartment house'

    @classmethod
    def choices(cls):
        return [(item.name, item.value) for item in cls]


class Floor(Enum):
    zero = 'Ground floor'
    first = '1 floor'
    second = '2 floor'
    third = '3 floor'
    fourth = '4 floor'
    fifth = '5 floor'
    sixth = '6 floor'
    seventh = '7 floor'
    eighth = '8 floor'
    ninth = '9 floor'
    higher = '> 9 floor'

    @classmethod
    def choices(cls):
        return [(item.name, item.value) for item in cls]


class Heat(Enum):
    district = 'District heating'
    gas = 'Gas heating'
    electric = 'Electric heating'
    boiler = 'Boiler'
    other = 'Other'

    @classmethod
    def choices(cls):
        return [(item.name, item.value) for item in cls]


class Equipment(Enum):
    fridge = 'Fridge'
    dishwasher = 'Dishwasher'
    tv = 'TV'
    washer = 'Washing machine'
    furniture = 'Furniture'
    stove = 'Stove'
    oven = 'Oven'
    balcony = 'Balcony'
    terrace = 'Terrace'
    elevator = 'elevator'
    ac = 'Air conditioning'

    @classmethod
    def choices(cls):
        return [(item.name, item.value) for item in cls]


class Province(Enum):
    Silesia = 'Silesia'

    @classmethod
    def choices(cls):
        return [(item.name, item.value) for item in cls]


class County(Enum):
    Wroclaw = 'Wroclaw'

    @classmethod
    def choices(cls):
        return [(item.name, item.value) for item in cls]


class City(Enum):
    Wroclaw = 'Wroclaw'

    @classmethod
    def choices(cls):
        return [(item.name, item.value) for item in cls]