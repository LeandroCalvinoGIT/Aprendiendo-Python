def esPrimo(numero):
    esPrimo = True

    for divisor in range(2,numero,1):
        if numero % divisor == 0:
            # print(f"El número {numero} es divisible por {divisor}")
            esPrimo = False

    if esPrimo:
        # print(f"El número {numero} es un número Primo :D")
        return True
    else:
        #print(f"El número {numero} NO es un número Primo :s")
        return False