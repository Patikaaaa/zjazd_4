liczba = input("podaj liczbę:\n")

for wiersz in range(int(liczba)+1):
    for kolumna in range(wiersz):
        print(kolumna + 1, end='')
    print()