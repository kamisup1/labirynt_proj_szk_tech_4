from collections import deque

from Labirynt.Algorytmy.baza import AlgorytmBazowy
from Labirynt.dekoratory import timer, log


class BFS(AlgorytmBazowy):
    @timer
    @log

    def przeszukaj(self):
        # przeszukuje labirynt algorytmem BFS i zwraca True,
        # jeśli istnieje ścieżka z lewego górnego rogu do prawego dolnego.

        wiersze = self.labirynt.wiersze
        kolumny = self.labirynt.kolumny
        siatka = self.labirynt.siatka

        #to tablica odwiedzonych pol zeby nie wracac w kolko
        odwiedzone = [[False for _ in range(kolumny)] for _ in range(wiersze)]
        #tablica rodzic do rekonstrukcji najkrotszej sciazki
        rodzic = [[None for _ in range(kolumny)] for _ in range(wiersze)]
        kolejka = deque() #kolejka do bfs
        kolejka.append((0,0)) #zaczynamy od 0,0
        odwiedzone[0][0] = True

        #lista mozliwych ruchow
        ruchy = [(-1,0), (1,0), (0,-1), (0,1)]

        #petla BFS DOPOKI KOLEJKA INE JEST PUSTA
        while kolejka:
            x, y = kolejka.popleft() #zdejmujemy z kolejki
            if(x, y) == (wiersze -1, kolumny -1): # if dodatrlismy na koniec to odtwarzamy cala sciezke
                sciezka = []
                cx, cy = x, y
                #cofamy sie po rodzicach az do startu - do narysowania potem sciezki
                while (cx, cy) != (0, 0):
                    sciezka.append((cx, cy))
                    cx, cy = rodzic[cx][cy]
                sciezka.append((0, 0)) #dodajemu start
                sciezka.reverse() #odwracamy sciezke od startu do mety
                print(f"[BFS] Znaleziono ścieżkę długości {len(sciezka) - 1}")
                print(f"[BFS] Ścieżka: {sciezka}")
                return sciezka

            # Sprawdzamy wszystkie możliwe sąsiednie pola
            for dx, dy in ruchy:
                nx, ny = x + dx, y + dy
                # czy pole w  jest  granicach i czy jest wolne i czy jescze nie jest odwiedozne
                if 0 <= nx < wiersze and 0 <= ny < kolumny:
                    if siatka[nx][ny] == 0 and not odwiedzone[nx][ny]:
                        odwiedzone[nx][ny] = True
                        rodzic[nx][ny] = (x, y)
                        kolejka.append((nx, ny))

            # jak wyszlo z petli to nie ma sciezki
        print("[BFS] Ścieżka NIE istnieje.")
        return None
