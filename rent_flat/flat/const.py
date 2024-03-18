from enum import Enum


class Rooms(Enum):
    One = '1'
    Two = '2'
    Three = '3'
    Four = '4'
    Five = '5'
    Six = '6'
    Seven = '7'
    Eight = '8'
    Nine = '9'
    Ten = '10'
    More = 'more than 10'

    @classmethod
    def choices(cls):
        return [(item.name, item.value) for item in cls]


class Development(Enum):
    House = 'Detached house'
    Block = 'Block'
    Tenement = 'Tenement house'
    Rowhouse = 'Rowhouse'
    SemiHouse = 'Semi-detached house'
    Loft = 'Loft'
    Apartment = 'Apartment house'

    @classmethod
    def choices(cls):
        return [(item.name, item.value) for item in cls]


class Floor(Enum):
    Zero = 'Ground floor'
    First = '1 floor'
    Second = '2 floor'
    Third = '3 floor'
    Fourth = '4 floor'
    Fifth = '5 floor'
    Sixth = '6 floor'
    Seventh = '7 floor'
    Eighth = '8 floor'
    Ninth = '9 floor'
    Higher = '> 9 floor'

    @classmethod
    def choices(cls):
        return [(item.name, item.value) for item in cls]


class Heat(Enum):
    District = 'District heating'
    Gas = 'Gas heating'
    Electric = 'Electric heating'
    Boiler = 'Boiler'
    Other = 'Other'

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


class District(Enum):
    Fabryczna = 'Fabryczna'
    Krzyki = 'Krzyki'
    PsiePole = 'Psie Pole'
    Srodmiescie = 'Srodmiescie'
    Jagodno = 'Jagodno'
    Nadodrze = 'Nadodrze'
    Rynek = 'Rynek'
    StareMiasto = 'Stare Miasto'


    @classmethod
    def choices(cls):
        return [(item.name, item.value) for item in cls]


class Status(Enum):
    Active = 'Active'
    Archive = 'Archive'


    @classmethod
    def choices(cls):
        return [(item.name, item.value) for item in cls]
