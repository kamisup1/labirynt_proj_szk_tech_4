from Labirynt.Algorytmy.baza import AlgorytmBazowy
from Labirynt.dekoratory import timer, log

#dfs czyli przeszukiwanie w glab - idzie w jednym kierunku jak najdalej sie da zanim sie cofnie
class DFS(AlgorytmBazowy):
    @timer
    @log
    def przeszukaj(self):
        wiersze = self.labirynt.wiersze
        kolumny = self.labirynt.kolumny
        siatka = self.labirynt.siatka

        #tablica odwiedzonych pol zeby nie wracac w kolko
        odwiedzone = [[False for _ in range(kolumny)] for _ in range(wiersze)]
        sciezka = [] #tu przechowywane w liscie - aktyalna trasa od startu do mety


        #funkcja rekurencyjna:
        def dfs(x,y):
            if not (0<= x < wiersze and 0 <= y < kolumny):
                return False #jesli pole jest poza plansza to nie kontynuujemy
            if siatka [x][y] == 1 or odwiedzone[x][y]:
                return False # jesli pole to sciana albo jest odwiedzone to nie kontynuujemy
            sciezka.append((x,y))
            odwiedzone[x][y] = True #dodajemy pole do sciezki i oznaczamy jako odwiedozne

            if (x,y) == (wiersze-1, kolumny-1):
                return True #dotarcie na koneic labiryntu KONEIC

            #we wszytkich kierunkach
            for dx,dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                if dfs(x+dx, y+dy):
                    return True #jelsi z sasiada da sie dojsc do maty to git - taka siezka bedzie ok

            # cofniecie jelsi sciezka w danym miejscu nie rpowadzi do celu
            sciezka.pop() #usuniecie ostatniego kroku z trasy bo tedy nie dojdziemy
            return False

        znaleziono = dfs(0,0) #start dfs od pola (0,0)

        if znaleziono:
            print(f"[DFS] Znaleziono ścieżkę długości {len(sciezka)-1}")
            print("[DFS] Ścieżka:", sciezka)
            return sciezka
        else:
            print("[DFS] Ścieżka NIE istnieje.")
            return None

