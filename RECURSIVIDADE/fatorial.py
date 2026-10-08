def fat(n):
    if n == 0: # Criterio de parada
        return 1
    elif n > 0: # Criterio recursivo
        return n * fat(n-1)


if __name__ ==  "__main__":
    resultado = fat(4)
    print(resultado)