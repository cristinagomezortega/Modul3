#Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo o la de un círculo.
#Si se contesta que se quiere calcular el área de un triángulo, el programa tiene que pedir entonces la base 
#y la altura y escribir el área. Si se contesta que se quiere calcular el área de un círculo, el programa tiene 
#que pedir entonces el radio y escribir el área.
#Se recuerda que el área de un triángulo es base por altura dividido por 2 y 
#que el área de un círculo es Pi (aproximadamente 3,141592) por el radio al cuadrado.

#Calculadora de áreas:
#-------------------------------
#T) Triángulo
#C) Círculo
#¿Qué figura quiere calcular (Escriba T o C)? T
#Escriba la base: 3
#Escriba la altura: 5.5
#Un triángulo de base 3.0 y altura 5.5 tiene un área de 8.25


#Calculadora de áreas:
#-------------------------------
#T) Triángulo
#C) Círculo
#¿Qué figura quiere calcular (Escriba T o C)? C
#Escriba el radio: 2
#Un círculo de radio 2.0 tiene un área de 12.566370614359172

#Pista:
#from math import pi
#perimetro=2*pi*radio
#Versión mejorada:
#Redondear el resultado del área a 2 decimales


figura=input("Que figura quiere calcular,escriba T o C:")
if (figura == "T"):
    base=int(input("Indique la base:"))
    altura=int(input("Indique la altura:"))
    area=(base*altura)/2
    print("La respuesta del triangulo es" ,area)
else:
    if (figura == "C"):
        radio=int(input("Indique el radio:"))
        perimetro=(3.14*radio**2)
