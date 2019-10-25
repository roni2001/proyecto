t=tuple("hola a todos")
print(t)
for i in range(6):
    a=str(input("ingrese la letra deseada:"))
    print("la letra es :",a in t)
print("el numero de letras es :",len(t))
print("el clonado de la tupla es :",t[:])
print("el conteo de las letras es de :",t.count(a))