import logging
logging.basicConfig(level=logging.DEBUG)
działanie = input("Padaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
try:
    a = eval(input("Podaj składnik 1: "))
    b = eval(input("Podaj składnik 2: "))
except NameError:
    print("Podaj poprawną liczbę")
    logging.info(f'Błędna liczba')
if działanie > '4':
    print("Wybierz poprawnie działanie")
    logging.info(f'Niema takiego działania')


def wynik(a,b):

    if działanie == '1':
        logging.info(f'Dodaje {a} i {b}')
        logging.info(f'Wynik to {a+b}')
        return a+b
    elif działanie == '2':
        logging.info(f'Odejmuje {a} i {b}')     
        logging.info(f'Wynik to {a-b}')
        return a-b
    elif działanie == '3':
        logging.info(f'Mnoże {a} i {b}')
        logging.info(f'Wynik to {a*b}')
        return a*b
    elif działanie == '4':
        logging.info(f'Dziele {a} przez {b}')
        if b == 0:
            logging.error("nie dzielimy przez zero")
        logging.info(f'Dziele {a} przez {b}')
        logging.info(f'Wynik to {a/b}')
        if wynik == 'Nie ma takiego działania':
            logging.error('Nie ma takiego działania')
        try: return a/b
        except ZeroDivisionError:
           return"Nie można dzielić przez 0"
    else:       
        return "Nie ma takiego działania"
    
print(wynik(a,b))
