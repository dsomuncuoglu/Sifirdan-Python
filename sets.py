fruits={"apple","banana","orange","dragon fruit","peace","melon"}

# print(fruits[0]) indexlenemez sets

global x
def printFruits(): # Ekrana yazdırma fonksiyonu
    x=1
    for i in fruits:
        print(str(x)+".Meyve => "+str(i))
        x+=1


# Ekleme işlemi
fruits.add("raspberry")
fruits.update(["mango","grape"]) # Dizi atama

printFruits() # Fonksiyon çağırma
print("\n")

# Silme İşlemi
fruits.remove("dragon fruit")
fruits.discard("melon")

printFruits()
print("\n")

fruits.pop() # Set'de sıra olmadığı için pop ile rastgele bir eleman silinebilir.

printFruits()
print("\n")

expList=[1,2,3,4,4,5,6,5,6,8]

print("Normal Liste= ",expList) # Normal liste
print("Set Kullanilmis Hali= ",set(expList)) # Set'in en önemli yanı tekrar eden verileri almaz.

