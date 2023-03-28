działanie = input("Padaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
a = eval(input("Podaj składnik 1: "))
b = eval(input("Podaj składnik 2: "))
wynik =0

if działanie == '1':
    wynik = a+b
elif działanie == '2':
    wynik = a-b
elif działanie == '3':
    wynik = a*b
elif działanie == '4':
    try:wynik = a/b
    except ZeroDivisionError:
        wynik="Nie można dzielić przez 0"
else:       
    wynik = "Nie ma takiego działania"

import logging
logging.basicConfig(level=logging.DEBUG)

if działanie == '1':
    logging.info(f'Dodaje {a} i {b}')
    logging.info(f'Wynik to {a+b}')
elif działanie == '2':
    logging.info(f'Odejmuje {a} i {b}')     
    logging.info(f'Wynik to {a-b}')
elif działanie == '3':
    logging.info(f'Mnoże {a} i {b}')
    logging.info(f'Wynik to {a*b}')
elif działanie == '4':
    logging.info(f'Dziele {a} i {b}')
    if b == 0:
        logging.error("nie dzielimy przez zero")
    else:
        logging.info(f'Wynik to {a/b}')
if wynik == 'Nie ma takiego działania':
    logging.error('Nie ma takiego działania')
print(wynik)
