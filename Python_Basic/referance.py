
#   Deniz Somuncuoglu

# value type => string, int and float

from tkinter import Y


x=10
y=25

x=y

y=10

print("X'in değeri",x)
print("Y'nin değeri",y)

# referance type => list, class exp.

a=["banana","apple"]
b=["banana","apple"]

a=b # İki listede bellekteki aynı adresi almasını sağlandı ve bu sayede birinde yapılan değişiklik sonucu diğer listeyide etkilemiş oldu.

b[0]="raspberry"

print(a,b)