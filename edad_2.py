jubilado=input("di si lo eres o no:"))
sexo=input("di tu sexo:")
cabello=input("indica eltipo de cabello que tienes:")
if(jubilado=="no")and(sexo=="hombre"):
    print("tienes que pagar 1 euro")
else:
    print("no tienes que pagar 1 euro")
if(jubilado=="si")and(sexo=="mujer")and(cabello=="morena"):
    print("no debes de pagar")
else:
    print("deberas de pagar")
if(jubilado=="si"):
    print("lo tienes gratis")
else:
    print("lo tienes que pagar")
