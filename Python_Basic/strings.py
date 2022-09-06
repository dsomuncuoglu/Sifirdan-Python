name,surname,age=("Deniz","Somuncuoğlu",23)

# \n alt satıra geçmek için kullanılır.
print(name+" "+surname+"\nYaşı="+str(age))

print(name[0])

print(len(name))

# Son karakteri verir.
print(name[len(name)-1])

# Son karakter alternatif
print(name[-1])





# Belirli karakter aralığı alma
print(name[0:3])
# alternatif
print(name[:3])
# İkişer artan olarak al
print(name[1:4:2]) # Deniz -> e ile i karakterlerini yazar.


