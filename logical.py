x=6
result=5<x<10

# Bu işlemleri "and", "or", "not" mantıksal ifadeler ile koşulu kurgulayabiliriz.

and_result=(x>5) and (x<10) # İki koşulunda sağlandığı.
or_result=(x>7) or (x<10)   # İki koşuldan birisinin sağlaması yeterlidir.
not_result=not(x>5)         # Koşulun tersini alan mantıksal ifadedir. 


print(f"and : {and_result}\nor : {or_result}\nnot : {not_result}")

# Kullanıcıdan istenen sayı 1 ile 100 arasında olan bir çift sayı mıdır?

inputUser=int(input("1 ile 100 arasında bir sayi girin = "))
if 1<inputUser<100:
    expResult=((inputUser>1) and (inputUser<100)) and (inputUser%2==0)
    print(f"Girilen sayi = {inputUser}\nGirilen sayi cift sayi midir? {expResult}")
else:
    print(f"Girilen sayi = {inputUser}.\nLutfen 1 ile 100 arasinda bir sayi giriniz!!!")
