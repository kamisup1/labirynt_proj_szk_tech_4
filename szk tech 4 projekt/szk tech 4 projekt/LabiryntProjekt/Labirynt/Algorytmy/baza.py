#zawiera metaklasę i klasę bazową dla wszystkich algorytmów przeszukujących labirynt.

class MetaAlgorytm(type):
    #metaklasa pilnuje jak sa tworzone klasy
    def __new__(cls, name, bases,dct):
        #sprawdza czy tworzone klasy maja metode przeszukaj
        if 'przeszukaj' not in dct:
            raise TypeError(f"Klasa {name} musi implementować metodę 'przeszukaj'.")
        return super().__new__(cls, name, bases, dct)

class AlgorytmBazowy(metaclass=MetaAlgorytm):
    #"fabryka" klas Lab 2 – Metaklasy
    def __init__(self, labirynt):
        self.labirynt = labirynt
    def przeszukaj(self):
        raise NotImplementedError("Każda podklasa musi zaimplementować tę metodę.")
