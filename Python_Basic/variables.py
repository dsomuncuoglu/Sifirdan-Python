
#   Deniz Somuncuoglu

maasAli=5000
maasAhmet=4000
vergi=0.27

netmaasAli=maasAli-(maasAli*vergi)
netmaasAhmet=maasAhmet-(maasAhmet*vergi)

print("Ali'nin net maasi=",netmaasAli)
print("Ahmet'in net maasi=",netmaasAhmet)

#*
# Değişken Tanımlama Kuralları
# 1-Rakam ile başlayamaz.
# 2-Büyük küçük harf duyarlılığı vardır.
# 3-Türkçe karakter kullanılmaz.
# *#



x=1             # int
y=2.3           # float
name="Deniz"    # string
isStudent=True  # bool

x,y,name,isStudent=(2,5.2,"DenizS",False)