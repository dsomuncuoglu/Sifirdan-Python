
#   Deniz Somuncuoglu


list_=[1,2,3]

tuple_=(1,'iki',3)

print(type(list_))
print(type(tuple_))

print(list_[1])
print(tuple_[1])

list_[0]="deniz"
'''tuple_[0]="ahmet" # Tuple işlemine sadece başta eleman atanabilir. Yani var olan değerin üstüne atama yapılamaz.'''

tuple_.index('iki')

# İki tuple'ı birleştirme.
names=("ayşe","fatma","hayriye")+tuple_

print(list_)
print(tuple_)
print(names)