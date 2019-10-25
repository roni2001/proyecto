a=set()
for e in range(6):
    x=float(input("ingrese la edad deseada:"))
    if x>=1 and x<=99:
        a.add(x)
    else:
        print("edad no admitible")
print("la cantidad de edades son:",len(a))
set(sorted(a))
print("las edades ordenadas son:",a)
