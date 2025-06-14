import random
class Labirynt:
    def __init__(self, wiersze, kolumny, gestosc=0.3):
        self.wiersze = wiersze
        self.kolumny= kolumny
        self.gestosc= gestosc
        self.siatka = self._generuj()

    def _generuj(self):
        #Tworzy dwuwymiarową listę z losowo rozmieszczonymi ścianami
        siatka = [
            [1 if random.random() < self.gestosc else 0 for _ in range(self.kolumny)]
            for _ in range(self.wiersze)
        ]
        # start i meta są zawsze o
        siatka[0][0] = 0
        siatka[self.wiersze - 1][self.kolumny - 1] = 0
        return siatka

    def wyswietl(self):
        #wypisuje labirynt w konsoli
        for wiersz in self.siatka:
            linia = ''.join(['#' if pole == 1 else 'o' for pole in wiersz])
            print(linia)

    def rysuj_sciezke(self, sciezka):
        #towrzenie kopii siatki, zeby nie zmieniac oryginalu:
        siatka_kopia = [row.copy() for row in self.siatka]
        for x,y in sciezka:
            siatka_kopia[x][y] = 2
        for row in siatka_kopia:
            print("".join([
                "#" if cell == 1 else
                "o" if cell == 2 else
                "." for cell in row
            ]))