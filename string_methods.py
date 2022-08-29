from traceback import print_tb


metin="Deniz Somuncuoglu"

buyuk=metin.upper() # Tüm metini büyük harf ile yazar
print(buyuk)
kucuk=metin.lower() # Tüm metini küçük harf ile yazar
print(kucuk)
baslik=metin.title() # Boşluktan sonraki ilk harfi büyük yazar.
print(baslik)
ilkHarfBuyuk=metin.capitalize() # Metindeki ilk harfi büyük yazar.
print(ilkHarfBuyuk)
split_=metin.split() # Metini böler ve dizi içerisine atar.
print(split_)
strip_=metin.strip()
print(strip_)
join_='*'.join(metin) # Harflerin arasına istenen karakteri ekler.
print(join_)
find_=metin.find("Som") # Metin içerisinde arama yapar.
print(find_)
isFoundStart=metin.startswith('D') # Metin istenen metin ile mi başlıyor? (True or False)
print(isFoundStart)
isFoundEnd=metin.endswith('u') # Metin istenen metin ile mi bitiyor? (True or False)
print(isFoundEnd)
replace_=metin.replace('Deniz','Ahmet') # Metin içerisinde değişiklik yapmak için kullanılır.
print(replace_)
center_=metin.center(50,'*') # Metini ortalamak için gerekli karakteri ekler.
print(center_)