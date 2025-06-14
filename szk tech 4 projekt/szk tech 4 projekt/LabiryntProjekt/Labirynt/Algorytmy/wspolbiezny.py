from multiprocessing import Pool

from Labirynt.Algorytmy.BFS import BFS
from Labirynt.Algorytmy.DFS import DFS
from Labirynt.Algorytmy.baza import AlgorytmBazowy
from Labirynt.dekoratory import timer, log


#funkcja uruchamiana w osobnych procesach, ktr=ora bierze args (luste argumentow - czyli u nas labirynt)
#dla kazdego procesu ta funkcja tworzy nowy obiekt bfs, uruchamia metode przeszukaj i zwraca wynik

def przeszukaj_fragment(args):
    # args to krotka zawierająca te elementy:
    labirynt, numer_procesu, Algorytm, alg_nazwa = args
    # Tworzymy nowy obiekt BFS albo DFS dla tego procesu, przekazując mu labirynt
    alg = Algorytm(labirynt)
    # Uruchamiamy przeszukiwanie labiryntu
    sciezka = alg.przeszukaj()

    #liczy dlugosc siezki
    dlugosc = len(sciezka) - 1 if sciezka else None

    # Wypisujemy komunikat KONIEC z wynikiem
    print(f"[Proces {numer_procesu} | {alg_nazwa}] Długość ścieżki: {dlugosc}")

    # Zwracamy wynik (True/False) do procesu GLOWNEGO
    return (alg_nazwa, sciezka is not None, dlugosc)


class Wspolbiezny(AlgorytmBazowy):
    @timer
    @log
    def przeszukaj(self): #metoda wymuszona przez klase bazowa mataalgorytm
        algorytmy = [
            (BFS, "BFS"),
            (DFS, "DFS"),
        ]

        liczba_procesow = len(algorytmy) #tyle bedzie procesow rownoleglych uruchomoinych
        argumenty = [(self.labirynt, i + 1, alg, nazwa)
                     for i, (alg, nazwa) in enumerate(algorytmy)] #to lista argumentów dla kazdego porcesu

        with Pool(liczba_procesow) as pool:
        #Pool uruchamia kilka porcesow równolegle - pula porcesow
            wyniki = pool.map(przeszukaj_fragment, argumenty)

        # podsumowanie: nazwa, czy znaleziono sciezke , dlugosc
        print("\n=== PODSUMOWANIE ===")
        for nazwa, czy_jest, dlugosc in wyniki:
            print(f"Algorytm: {nazwa} | Czy ścieżka wystepuje? {czy_jest} | Długość: {dlugosc}")

        # zwracamy true jesli chociaz jeden alg znalazl sciezke
        return any(w[1] for w in wyniki)