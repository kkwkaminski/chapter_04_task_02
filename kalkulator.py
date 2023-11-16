import logging

def dodawanie(*args):
    return sum(args)

def odejmowanie(a, b):
    return a - b

def mnozenie(*args):
    result = 1
    for arg in args:
        result *= arg
    return result

def dzielenie(a, b):
    if b != 0:
        return a / b
    else:
        return "Nie można dzielić przez zero!"


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    print("Podaj działanie, posługując się odpowiednią liczbą:")
    print("1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
    str_operation= ['Dodaję:', 'Odejmuję:','Mnożę:', 'Dzielę:']
    operation = int(input())
    
    if operation in [1, 2, 3, 4]:
        logging.info("Wybrano operację: %s", operation)
        
        if operation in [1, 3]:  # Dodawanie lub mnożenie
            logging.info("Podaj składniki oddzielone spacją:")
            components = [float(x) for x in input().split()]
            logging.info(f"{str_operation[operation-1]} {', '.join(map(str, components)) if len(components) > 1 else components[0]}")
        else:  # Odejmowanie lub dzielenie
            logging.info("Podaj składnik 1:")
            component1 = float(input())
            logging.info("Podaj składnik 2:")
            component2 = float(input())
            logging.info(f"{str_operation[operation-1]} {component1} i {component2}")

        if operation == 1:
            result = dodawanie(*components)
        elif operation == 2:
            result = odejmowanie(component1, component2)
        elif operation == 3:
            result = mnozenie(*components)
        else:
            result = dzielenie(component1, component2)

        print("Wynik to:", result)
    else:
        print("Niepoprawny numer operacji. Spróbuj ponownie.")