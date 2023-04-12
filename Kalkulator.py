import logging
logging.basicConfig(level=logging.DEBUG)
def menu():
    choice = input("Padaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    if choice > '4':
        print("Wybierz poprawnie działanie")
        logging.info(f'Niema takiego działania')
    a = eval(input("Podaj składnik 1: "))
    b = eval(input("Podaj składnik 2: "))
    result = calc(choice,a,b)
    print(result)


def add(a,b):
    logging.info(f'Dodaje {a} i {b}')
    logging.info(f'Wynik to {a+b}')
    return a+b

def subtract(a,b):
    logging.info(f'Odejmuje {a} i {b}')     
    logging.info(f'Wynik to {a-b}')
    return a-b

def multiply(a,b):
    logging.info(f'Mnoże {a} i {b}')
    logging.info(f'Wynik to {a*b}')
    return a*b

def divide(a,b):
    logging.info(f'Dziele {a} przez {b}')
    if b == 0:
        logging.error("nie dzielimy przez zero")
    logging.info(f'Dziele {a} przez {b}')
    logging.info(f'Wynik to {a/b}')
    try: return a/b
    except ZeroDivisionError:
        return"Nie można dzielić przez 0"
def calc(choice,a,b):
    choices = {'1':add, '2':subtract, '3':multiply, '4':divide}
    method = choices.get(choice)
    if method:
        return method(a,b)
    
    
print(menu())

    
    
  

    
 

