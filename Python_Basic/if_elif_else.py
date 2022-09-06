
sayi1=int(input("Birinci sayiyi girin = "))
sayi2=int(input("İkinci sayiyi girin = "))

if sayi1>sayi2:
    print(f"{sayi1}>{sayi2}\nBirinci sayi ikinci sayidan büyüktür.")
elif sayi2>sayi1:
    print(f"{sayi2}>{sayi1}\İkinci sayi birinci sayidan büyüktür.")
else:
    print(f"{sayi1}={sayi2}\nBirinci sayi ikinci sayiya esittir.")
