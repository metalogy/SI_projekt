from experta import *

#Warunki uprawy
class SoilPH(Fact):
    #INFO- zmienne
    # acidic
    # neutral
    # alkaline
    #DNM - doesnt matter, użytkownikowi wszystko jedno
    pass

class Humidity(Fact):
    #INFO- zmienne
    # wet
    # moderate
    # dry
    #DNM - doesnt matter, użytkownikowi wszystko jedno
    pass

class Insolation(Fact):
    #INFO- zmienne
    # sunny
    # moderate
    # dark
    #DNM - doesnt matter, użytkownikowi wszystko jedno
    pass

#Preferencje użytkownika, warunki wizualne i użytkowe
class Size(Fact):
    #INFO- zmienne
    # big
    # moderate
    # small
    #DNM - doesnt matter, użytkownikowi wszystko jedno
    pass

class Function(Fact):
    #INFO- zmienne
    # decorative
    # aromatic
    # edible
    #DNM - doesnt matter, użytkownikowi wszystko jedno
    pass

class Alergic(Fact):
    #INFO- zmienne
    # non_alergic
    # alergic
    #DNM - doesnt matter, użytkownikowi wszystko jedno
    pass

class PrimaryColor(Fact):
    #TODO-WYPEŁNIĆ KOLORY
    pass

class SecondaryColor(Fact):
    # TODO-WYPEŁNIĆ KOLORY
    pass
