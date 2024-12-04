zadania = [
    {'czas': 4, 'nagroda': 10},
    {'czas': 2, 'nagroda': 5},
    {'czas': 1, 'nagroda': 3},
    {'czas': 3, 'nagroda': 8},
]


def procedur(zadania):
    zadania.sort(key=lambda x: x['czas'])

    czas_oczekiwania = 0
    aktualny_czas = 0
    kolejnosc = []
    for zadanie in zadania:
        kolejnosc.append(zadanie)
        czas_oczekiwania += aktualny_czas
        aktualny_czas += zadanie['czas']

    return kolejnosc, czas_oczekiwania


kolejnosc, czas_oczekiwania = procedur(zadania)
print("Kolejność zadań:", kolejnosc)
print("Czas oczekiwania:", czas_oczekiwania)
