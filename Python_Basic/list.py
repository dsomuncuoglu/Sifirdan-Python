
#   Deniz Somuncuoglu

my_list=[1,2,3]
print(my_list)
my_list2=["bir",2,True,5.2]
print(my_list2)

list1=["bir","iki","üç"]
list2=["dört","beş","altı"]

toplamlist=list1+list2
print(toplamlist)
print(toplamlist[2]) # Toplam listesinin 3. elemanını verir.
print(len(toplamlist)) # Toplam eleman sayısı


# İç içe liste oluşturma

userA=["Furkan",30]
userB=["Deniz",24]

users=[userB,userA]

print(users) # Liste içi liste tüm bilgiler
print(users[0]) # Birinci elemanın bilgileri
print(users[0][0]) # Birinci elemanın adi
print(users[1][1]) # İkinci elemanın yaşı






