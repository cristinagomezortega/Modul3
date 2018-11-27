Dividiendo=int(input("Escriba el numero que usted quiera:"))
Divisor=int(input("Escriba el numero que usted quiera:"))

if Divisor ==0:
    print("La division es aceptable,pero no tiene logica")
else: 
    if Dividiendo % Divisor ==0:
        print("La divisio es exacta")
    else:
        print("La division no es exacta")
