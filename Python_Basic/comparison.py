# DB => username="deniz",
#       password="12345"
# 
#*  Eğer username ve password program kullanıcısının girdiği veriler ile uyuşuyorsa 
#       Giriş sağlanır.
#   Eğer username ve password program kullanıcısının girdiği veriler ile uyuşmuyorsa
#       Giriş sağlanmaz. (Kullanici adi ve sifre yanlis hatası gösterilir.)
# *#

from unittest import result


username="deniz"
password="12345"

input_username=(input("Kullanici adini girin= "))
input_password=(input("Sifreyi girin= "))

result_u=(input_username==username)
result_p=(input_password==password)

if result_u and result_p is True:
    print("Giriş Sağlandı. Hoşgeldin ",username.upper())
else:
    print("Kullanici adi ve parolanız yanlış tekrar deneyin.")

a,b,c=5,5,10

print("A B'ye eşit midir?",a==b)
print("A B'den büyük müdür?",a>b)
print("A B'den büyük eşit midir?",a>=b)
print("A B'ye eşit değil midir?",a!=b)
print("A B'den küçük müdür?",a<b)
print("A B'den küçük eşit midir?",a<=b)

print("A C'ye eşit midir?",a==c)
print("A C'den büyük müdür?",a>c)
print("A C'den büyük eşit midir?",a>=c)
print("A C'ye eşit değil midir?",a!=c)
print("A C'den küçük müdür?",a<c)
print("A C'den küçük eşit midir?",a<=c)

print(True==1) # True sayisal değer olarak 1'e eşittir.
print(False==1) # False sayisal değer olarak 2'ye eşittir.

result_TF=False+True+50
#           0  +  1 + 50   result=51 
print(result_TF)