
#   Deniz Somuncuoglu

# key - value mantığı ile çalışır

# 16 => Bursa, 34 => İstanbul temsil ediyor.

sehirler=["bursa","istanbul"]
plakalar=[16,34]

# Dictionary kullanmadan list ile yapım
print(plakalar[sehirler.index("bursa")])

# İstenen plakalar["bursa"] => 16 vermesi
# İstenen plakalar["istanbul"] => 34 vermesi

plakalarDic={"bursa":17,
            "istanbul":34}

print("Plakası istenen il: "+sehirler[0].upper()+" Plakası =>",plakalarDic["bursa"])
print("Plakası istenen il: "+sehirler[1].upper()+" Plakası =>",plakalarDic["istanbul"])

# Dictionary'ye yeni eleman ekleme veya değiştirme
plakalarDic["ankara"]=6
plakalarDic["düzce"]=81
plakalarDic["bursa"]=16 # Üst tarafta yanlış olan "17" değerini düzeltme

print("Mevcut Şehir ve Plakalar =",plakalarDic)

users={
    "denizsomuncuoglu":{
        "age":24,
        "roles":{
            "admin":"Yazılımcı",
            "yetki":"Program"
        },
        "mail":"deniz@gmail.com",
        "address":"bursa",
        "phone":"53125464"
    },
    "furkanenespolatoglu":{
        "age":30,
        "roles":{
            "admin":"Yönetici",
            "yetki":"Sistem"
        },
        "mail":"furkan@gmail.com",
        "address":"bursa",
        "phone":"535454545"
    }
}

print(users["denizsomuncuoglu"]["roles"])
print(users["denizsomuncuoglu"]["roles"]["yetki"])
