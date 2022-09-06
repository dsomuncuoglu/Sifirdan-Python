
#   Deniz Somuncuoglu


# Identity Operator: is (ayni bellek alanini isaret eder) not is (ayni bellek alanini isaret etmez.)

x=y=[1,2,3]
z=[1,2,3]

print(x==y)
print(x==z)

print(x is y)
print(f"x in degeri {x} z nin degeri {z} x ile z ayni obje mi? {x is z}") # Değer olarak eşit fakat farklı bellek kısımlarında bulundukları için False verir.

# Membership Operator: in (içerir.) not in (içermez.)

fruits=["banana","apple","grape"]
arananKelime="banana"
print(f"Fruits = {fruits} icerisinde '{arananKelime}' var mıdır?\nCevap = {arananKelime in fruits}") # Fruits içerisinde "banana" var mı?