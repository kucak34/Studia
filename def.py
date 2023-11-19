def wspolczynnik(wiek, waga, samopoczucie):
    wsp = 0
    if 50 > wiek > 18:
        wsp += 3

    if 95 > waga > 55:
        wsp += 3

    wsp += samopoczucie

    return wsp


wiek = int(input('Wprowadz wiek: '))
waga = int(input('Podaj mase ciala: '))
samopoczucie = int(input('Jak sie czujesz w skali o 1 do 10?: '))

wsp = wspolczynnik(wiek, waga, samopoczucie)

print(f'wynik to: {wsp}')

if wsp > 10:
    print('Super jest zdrow, damy ubezpieczenie')
else:
    print('Niestety nie mozemy dac ubezpieczenia')
