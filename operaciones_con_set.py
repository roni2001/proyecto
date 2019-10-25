#creacion
print("creacion")
a={12,10}
b=set("hola")
c=set(range(0,11))
d={1,2,3,4}
e=set("hoy es el gran dia ")
f={"naranja","mango","uva","higo"}
g={"lun","mar","mie","jue","vie"}
h=set(range(0,20,2))
i=set("hola mundo")
j=set()
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
#pertenecia:
print("pertenecia")
a={1,2,3,4,5,6,7,"hola"}
b=set("hola mundo")
c=set(range(1,190))
d=set("buenas noches")
e={"mago","lima","uva"}
f=set(range(123,900,5))
g=set("pragramacion el curso mas inportante de la carrera de electronica")
h={234445,5758,55}
i=set("abcdert")
j=set(range(1,400,12))
print(1 in a)
print("h" in b)
print(188 in c)
print("b" in d)
print("mago" in e)
print("a" not in f)
print(234445 not in g)
print(234445 not in h)
print("a" not in i)
print("a" not in j)
#comparacion
print("comparcion")
a={12,10}
c=set(range(0,11))
d={1,2,3,4}
e={"mago","lima","uva"}
f=set(range(123,900,5))
g=set("pragramacion el curso mas inportante de la carrera de electronica")
h={234445,5758,55}
i=set("abcdert")
j=set(range(1,400,12))
print(a<b)
print(b==c)
print(d<e)
print(g>a)
print(a<d)
print(j==i)
print(g>a)
print(a==i)
print(i>g)
print(a==e)
print(b>j)
#longitud
print("longitud")
a={12,10}
b=set("hola")
c=set(range(0,11))
d={1,2,3,4}
e=set("hoy es el gran dia ")
f={"naranja","mango","uva","higo"}
a={12,10}
b=set(range(0,11))
d={1,2,3,4}
e={1122,123,2214}
f=set(range(111,19238,45))
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))
print(len(g))
print(len(h))
print(len(i))
print(len(j))
#iteracion
print("iteracion")
a={12,10}
b=set("hola")
c=set(range(0,11))
d={1,2,3,4}
e={"mago","lima","uva"}
f=set(range(123,190,5))
g=set("pragramacion el curso mas inportante de la carrera de electronica")
h={234445,5758,55}
i=set("abcdert")
j={"naranja","mango","uva","higo"}
for k in a:
    print(k)
for l in b:
    print(l)
for m in c:
    print(m)
for n in d:
    print(n)
for ñ in e:
    print(ñ)
for o in f:
    print(o)
for p in g:
    print(p)
for q in h:
    print(q)
for r in i:
    print(r)
for s in j:
    print(s)
#maximos y minimos
print("maximos y minimos")
a={12,10}
b=set(range(0,11))
d={1,2,3,4}
e={1122,123,2214}
f=set(range(111,19238,45))
g={1,2,3,4,3,3,45,5,55,66}
h=set(range(0,20,2))
i=set(range(123,3456,8))
j={122222,2335,33,3,3}
c=set(range(12,5668,5))
print(max(a))
print(max(b))
print(max(c))
print(max(d))
print(max(e))
print(min(f))
print(min(g))
print(min(h))
print(min(i))
print(min(j))
#eleminacion:
print("eleminacion")
a={12,10}
b=set("hola")
c=set(range(0,11))
d={1,2,3,4}
e={"mago","lima","uva"}
f=set(range(123,900,5))
g=set("pragramacion el curso mas inportante de la carrera de electronica")
h={234445,5758,55}
i=set("abcdert")
j={"naranja","mango","uva","higo"}
#clonado:
print("clonado")
w={12,10}
b=set(range(0,11))
d={1,2,3,4}
e={1122,123,2214}
f=set(range(111,19238,45))
g={"lun","mar","mie","jue","vie"}
h=set(range(0,20,2))
i=set("hola mundo")
j=set()
print(w.copy())
print(b.copy())
print(c.copy())
print(d.copy())
print(e.copy())
print(f.copy())
print(g.copy())
print(h.copy())
print(i.copy())
print(j.copy())
#extraccion
print("extraccion")
a={12,10}
b=set("hola")
c=set(range(0,11))
d={1,2,3,4}
e=set("hoy es el gran dia ")
f={"naranja","mango","uva","higo"}
g={"lun","mar","mie","jue","vie"}
h=set(range(0,20,2))
i=set("hola mundo")
j={111,12}
print(a.pop())
print(b.pop())
print(c.pop())
print(d.pop())
print(e.pop())
print(f.pop())
print(g.pop())
print(h.pop())
print(i.pop())
print(j.pop())
#eleminacion
print("eleminacion")
a={1,2,3,4,5,6,7,"hola"}
b=set("hola mundo")
c=set(range(1,190))
d=set("buenas noches")
e={"mago","lima","uva"}
f=set(range(123,190,5))
g=set("programacion el curso mas inportante de la carrera de electronica")
h={234445,5758,55}
i=set("abcdert")
j=set(range(1,40,12))
a.discard(1)
print(a)
b.discard("o")
print(b)
c.discard(189)
print(c)
d.discard("b")
print(d)
e.discard("lima")
print(e)
f.discard(128)
print(f)
g.discard(r)
print(g)
h.discard(55)
print(h)
i.discard(13)
print(i)
#agregado
print("agregado")
a={12,10}
c=set(range(0,11))
b={"hola"}
d={1,2,3,4}
e={"mago","lima","uva"}
f=set(range(123,900,5))
g=set("pragramacion el curso mas inportante de la carrera de electronica")
h={234445,5758,55}
i=set("abcdert")
j=set(range(1,400,12))
a.add(134)
print(a)
b.add("a todos")
print(b)
c.add(14)
print(c)
d.add(5)
print(d)
e.add("naranja")
print(e)
f.add(901)
print(f)
g.add("dos")
print(g)
h.add(23345)
print(h)
i.add(123)
print(i)
j.add(401)
print(j)
#anulacion
print("anulacion")
a={12,10}
b=set("hola")
c=set(range(0,11))
d={1,2,3,4}
e=set("hoy es el gran dia ")
f={"naranja","mango","uva","higo"}
g={12,10}
h=set(range(0,11))
i={1,2,3,4}
j={1122,123,2214}
h.clear()
print(i)
j.clear()
print(h)
g.clear()
print(g)
f.clear()
print(f)
e.clear()
print(e)
d.clear()
print(d)
c.clear()
print(c)
b.clear()
print(b)
a.clear()
print(a)
j.clear()
print(j)
#separacion
print("separacion")
a={12,10}
b={12234,11}
c=set(range(0,11))
d={1,2,3,4}
e={"mago","lima","uva"}
f=set(range(123,900,5))
g=set("pragramacion el curso mas inportante de la carrera de electronica")
h={234445,5758,55}
i=set("abcdert")
j=set(range(1,400,12))
a.remove(12)
print(a)
b.remove(11)
print(b)
c.remove(5)
print(c)
d.remove(3)
print(d)
e.remove("mago")
print(e)
f.remove(128)
print(f)
g.remove("a")
print(g)
h.remove(55)
print(h)
i.remove("a")
print(i)
j.remove(1)
print(j)
#ordenDO
print("ordenado")
a={12,10}
b=set(range(0,11))
d={1,2,3,4}
e={1122,123,2214}
f=set(range(1123,11243,-45))
g={1,2,3,4,3,3,45,5,55,66}
h=set(range(0,20,2))
i=set(range(123,345,8))
j={122222,2335,33,3,3}
c=set(range(12,56,5))
x=set(sorted(a))
print(x)
y=set(sorted(b))
print(y)
t=set(sorted(c))
print(t)
w=set(sorted(d))
print(w)
s=set(sorted(e))
print(s)
v=set(sorted(f))
print(v)
k=set(sorted(g))
l=set(sorted(h))
print(l)
m=set(sorted(i))
print(m)
n=set(sorted(j))
print(j)
#union
print("union")
a={12,10}
b=set(range(0,11))
d={1,2,3,4}
e={1122,123,2214}
f=set(range(1123,11243,-45))
g={1,2,3,4,3,3,45,5,55,66}
h=set(range(0,20,2))
i=set(range(123,345,8))
j={122222,2335,33,3,3}
c=set(range(12,56,5))
k=a.union(b)
print(k)
l=b.union(c)
print(l)
m=c.union(a)
print(m)
n=d.union(b)
print(n)
ñ=e.union(c)
print(ñ)
o=f.union(a)
print(o)
p=g.union(b)
print(p)
q=h.union(a)
print(q)
r=i.union(b)
print(r)
s=j.union(g)
print(s)
#diferencia
print("diferencia")
a={12,10}
b=set(range(0,11))
d={1,2,3,4}
e={1122,123,2214}
f=set(range(1123,11243,-45))
g={1,2,3,4,3,3,45,5,55,66}
h=set(range(0,20,2))
i=set(range(123,345,8))
j={122222,2335,33,3,3}
c=set(range(12,56,5))
print(a-b)
print(d-b)
print(d-b)
print(g-b)
print(h-b)
print(i-f)
print(c-a)
print(e-d)
print(f-e)
print(e-c)
#interseccion
print("interseccion")
a={12,10}
b=set("hola")
c=set(range(0,11))
d={1,2,3,4}
e={"mago","lima","uva"}
f=set(range(123,190,5))
g=set("pragramacion el curso mas inportante de la carrera de electronica")
h={234445,5758,55}
i=set("abcdert")
j={"naranja","mango","uva","higo"}
print(a & c)
print(a & b)
print(g & b)
print(e & c)
print(g & i)
print(g & h)
print(a & i)
print(i & b)
print(a & j)
print(h & c)
print(a & f)
#diferencia simetrica
print(" diferencia simtrica")
a={1,2,3,4,5,6,7,"hola"}
b=set("hola mundo")
c=set(range(1,45))
d=set("buenas noches")
e={"mago","lima","uva"}
f=set(range(123,200,5))
g=set("pragramacion el curso mas inportante de la carrera de electronica")
h={234445,5758,55}
i=set("abcdert")
j=set(range(1,100,12))
print(a ^ b)
print(b ^ d)
print(c ^ e)
print(d ^ f)
print(h ^ g)
print(a ^ i)
print(j ^ a)
print(c ^ j)
print(d ^ a)
print(e ^ a)
print(j ^ d )