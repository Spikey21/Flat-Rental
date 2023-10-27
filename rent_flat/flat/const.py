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
    LowSilesia = 'Lower Silesia'
    Kuyavia = 'Kuyavia-Pomerania'
    Silesia = 'Silesia'
    Lodzkie = 'Lodzkie'
    Lublin = 'Lublin'
    Lubusz = 'Lubusz'
    LessPoland = 'Lesser Poland'
    Masovia = 'Masovia'
    Subcarpathia = 'Subcarpathia'
    Pomerania = 'Pomerania'
    WarmMasuria = 'Warmia-Masuria'
    GreatPoland = 'Greater Poland'
    WestPomerania = 'West Pomerania'

    @classmethod
    def choices(cls):
        return [(item.name, item.value) for item in cls]


class County(Enum):
    Warsaw = 'Warsaw'
    Wroclaw = 'Wroclaw'
    Cracow = 'Cracow'
    Gdansk = 'Gdansk'
    Poznan = 'Poznan'
    Szczecin = 'Szczecin'
    Gdynia = 'Gdynia'
    Czestochowa = 'Czestochowa'
    Opole = 'Opole'
    Lodz = 'Lodz'
    Bialystok = 'Bialystok'
    Katowice = 'Katowice'
    Tarnov = 'Tarnov'
    Krosno = 'Krosno'
    Rzeszow = 'Rzeszow'
    Glwice = 'Gliwice'
    Radom = 'Radom'
    ZielonGora = 'Zielona Gora'
    Lublin = 'Lublin'
    Swinoujscie = 'Swinoujscie'
    Bydgoszcz = 'Bydgoszcz'
    JeleniaGora = 'Jelenia Gora'
    Legnica = 'Legnica'
    Grudziadz = 'Grudziadz'
    Torun = 'Torun'
    Plock = 'Plock'
    Chorzow = 'Chorzów'
    Tychy = 'Tychy'
    Bytom = 'Bytom'
    Sosnowiec = 'Sosnowiec'
    Zabrze = 'Zabrze'
    Kielce = 'Kielce'
    Olsztyn = 'Olsztyn'
    Leszno = 'Leszno'
    Kalisz = 'Kalisz'
    Koszalin = 'Koszalin'

    @classmethod
    def choices(cls):
            return [(item.name, item.value) for item in cls]


class City(Enum):
    Warsaw = 'Warsaw'
    Wroclaw = 'Wroclaw'
    Cracow = 'Cracow'
    Gdansk = 'Gdansk'
    Poznan = 'Poznan'
    Szczecin = 'Szczecin'
    Gdynia = 'Gdynia'
    Czestochowa = 'Czestochowa'
    Opole = 'Opole'
    Lodz = 'Lodz'
    Bialystok = 'Bialystok'
    Katowice = 'Katowice'
    Tarnov = 'Tarnov'
    Krosno = 'Krosno'
    Rzeszow = 'Rzeszow'
    Glwice = 'Gliwice'
    Radom = 'Radom'
    ZielonGora = 'Zielona Gora'
    Lublin = 'Lublin'
    Swinoujscie = 'Swinoujscie'
    Bydgoszcz = 'Bydgoszcz'
    JeleniaGora = 'Jelenia Gora'
    Legnica = 'Legnica'
    Grudziadz = 'Grudziadz'
    Torun = 'Torun'
    Plock = 'Plock'
    Chorzow = 'Chorzów'
    Tychy = 'Tychy'
    Bytom = 'Bytom'
    Sosnowiec = 'Sosnowiec'
    Zabrze = 'Zabrze'
    Kielce = 'Kielce'
    Olsztyn = 'Olsztyn'
    Leszno = 'Leszno'
    Kalisz = 'Kalisz'
    Koszalin = 'Koszalin'


    @classmethod
    def choices(cls):
        return [(item.name, item.value) for item in cls]


class Status(Enum):
    Active = 'Active'
    Archive = 'Archive'


    @classmethod
    def choices(cls):
        return [(item.name, item.value) for item in cls]
