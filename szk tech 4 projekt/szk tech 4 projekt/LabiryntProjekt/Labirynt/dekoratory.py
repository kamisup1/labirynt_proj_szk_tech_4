import time

#dekokrator mierzacy czas dzialania funkcji
def timer(funkcja):
    def wrapper(*args, **kwargs):
        start = time.time()
        wynik = funkcja(*args, **kwargs)
        time.sleep(2) #opoznenie bo ta funckja trwa 0 sekund xd
        end = time.time()
        print(f"[TIMER] Funkcja trwała {end - start:.3f} sekund")
        return wynik
    return wrapper

#dekorator do logowania startu i konca funkcji
def log(funkcja):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Start funkcji: {funkcja.__name__}")
        wynik = funkcja(*args, **kwargs)
        print(f"[LOG] Koniec funkcji: {funkcja.__name__}")
        return wynik

    return wrapper