a=[]
b=1

for i in range(5):
    x= float(input("ingrese la nota del curso de programacion:"))
    if x>=0 and x<=20:
        a.append(x)
        print("la nota minima es de ",min(a))
        print("la nota maxima es de ", max(a))
        print("las notas ingresadas son :",len(a))

    else:
        print("nota no admitibe")
print(a)


