numbers=[1,3,4,56,10,5,34,44,10,88,-15,-1]
letters=['a','g','c','y','b','c','z','t','c','k']

minNumbersVal=min(numbers)
maxNumbersVal=max(numbers)
minLettersVal=min(letters)
maxLettersVal=max(letters)

print(minNumbersVal)
print(maxNumbersVal)
print(minLettersVal)
print(maxLettersVal)

print("Sayilar(4 den 7'ye kadar)=",numbers[3:6])
print("Sayilar(baştan 3'e kadar)=",numbers[:3])
print("Sayilar(4 den sona kadar)=",numbers[4:])

# append metodu ile listenin sonuna değer ekleme
numbers.append(49)
numbers.append(9)

print(numbers)

# insert ile listenin istediğimiz yere değer ekleme
numbers.insert(4,40)
numbers.insert(len(numbers),38) # insert ile sona değer eklemek istediğimizde len(list) ile ekleriz.
numbers.insert(-1,45) # insert ile sondan birinci değere eklemek istersek -1 kullanılır

print(numbers)

# Listeden eleman çıkarma
numbers.pop() # sondan eleman çıkarma
numbers.pop(0) # index değeri 0 olan elemanı çıkar
numbers.pop(-1) # index değeri -1 olan elemanı çıkar

print(numbers)

numbers.remove(34) # Listede yazılan eleman değeri var ise elemanı çıkarır.

print(numbers)

# Liste sıralanması
numbers.sort()
letters.sort()

print(numbers)
print(letters)

# Listenin tersine çevrilmesi
numbers.reverse()
letters.reverse()

print(numbers)
print(letters)

# Listenin eleman sayısını öğrenmek için len(list) kullanılır.
print(len(numbers))
print(len(letters))

# Liste içerisinde kullanıcının istediği değerden kaç adet olduğunu count() ile öğrenebiliriz.
print(numbers.count(10)) # 10 sayısından 2 adet mevcut
print(letters.count('c')) # c'den 3 adet mevcut

# Listeyi tamamen temizleme işlemi
numbers.clear()
letters.clear()
print(numbers)
print(letters)




