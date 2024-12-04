def podzielPaczki(wagi, max_waga):
    for waga in wagi:
        if waga > max_waga:
            raise ValueError(f"Paczka o wadze {waga} przekracza max dozwolona wage kursu ({max_waga} kg).")
        wagi_sort = sorted(wagi, reverse=True)
        kursy = []
    for waga in wagi_sort:
        dodano = False
    for kurs in kursy:
        if sum(kurs) + waga <= max_waga:
            kurs.append(waga)
            dodano = True
            break
    if not dodano:
        kursy.append([waga])
    return len(kursy), kursy


wagi = [21, 5, 8, 15, 10, 10, 7]
max_wag = 25

print(podzielPaczki(wagi, max_wag))

liczba_kursow, kursy = podzielPaczki(wagi, max_wag)
for i, kurs in enumerate(kursy, 1):
    print(f"Kurs {i} : {kurs} - suma wagi : {sum(kurs)} kg")




