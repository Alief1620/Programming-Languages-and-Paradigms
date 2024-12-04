Zadania: (czas_rozpoczecia, czas_zakonczenia, nagroda)
zadania = [
    (1, 4, 5),
    (3, 5, 1),
    (0, 6, 8),
    (5, 7, 8),
    (3, 9, 6),
    (5, 9, 4),
    (6, 10, 2),
    (8, 11, 4)
]


def procedur(zadania):
    zadania.sort(key=lambda x: x[1])
    wybrane_zadania = []
    maks_nagroda = 0
    ostatnie_zakonczenie = 0

    for zadanie in zadania:
        start, koniec, nagroda = zadanie
        if start >= ostatnie_zakonczenie:
            wybrane_zadania.append(zadanie)
            maks_nagroda += nagroda
            ostatnie_zakonczenie = koniec

    return maks_nagroda, wybrane_zadania


maks_nagroda, wybrane_zadania = procedur(zadania)
print("Maksymalna nagroda:", maks_nagroda)
print("Wybrane zadania:", wybrane_zadania)
