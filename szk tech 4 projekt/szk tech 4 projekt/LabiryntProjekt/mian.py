from Labirynt.Algorytmy.BFS import BFS
from Labirynt.Algorytmy.DFS import DFS
from Labirynt.Algorytmy.wspolbiezny import Wspolbiezny
from Labirynt.Labirynt import Labirynt

if __name__ == "__main__":
    # Ustaw parametry labiryntu
    WIERSZE = 50
    KOLUMNY = 50
    GESTOSC = 0.3

    # Tworzymy jeden labirynt i kopiujemy go dla każdego algorytmu (żeby testować dokładnie ten sam układ)
    l_bfs = Labirynt(wiersze=WIERSZE, kolumny=KOLUMNY, gestosc=GESTOSC)
    l_dfs = Labirynt(wiersze=WIERSZE, kolumny=KOLUMNY, gestosc=GESTOSC)
    l_wsp = Labirynt(wiersze=WIERSZE, kolumny=KOLUMNY, gestosc=GESTOSC)

    # Kopiujemy siatkę, żeby labirynty były IDENTYCZNE
    l_dfs.siatka = [row.copy() for row in l_bfs.siatka]
    l_wsp.siatka = [row.copy() for row in l_bfs.siatka]

    print("\n================= LABIRYNT =================")
    l_bfs.wyswietl()

    # Algorytm BFS
    print("\n========== Wynik BFS ==========")
    bfs_alg = BFS(l_bfs)
    bfs_sciezka = bfs_alg.przeszukaj()
    if bfs_sciezka:
        print("\nLabirynt ze ścieżką BFS:")
        l_bfs.rysuj_sciezke(bfs_sciezka)
    else:
        print("Nie znaleziono ścieżki BFS.")

    # Algorytm DFS
    print("\n========== Wynik DFS ==========")
    dfs_alg = DFS(l_dfs)
    dfs_sciezka = dfs_alg.przeszukaj()
    if dfs_sciezka:
        print("\nLabirynt ze ścieżką DFS:")
        l_dfs.rysuj_sciezke(dfs_sciezka)
    else:
        print("Nie znaleziono ścieżki DFS.")

    # Algorytm współbieżny (porównuje różne algorytmy na tym samym labiryncie)
    print("\n========== Wynik współbieżny (BFS vs DFS) ==========")
    alg_wsp = Wspolbiezny(l_wsp)
    alg_wsp.przeszukaj()