from unittest import result


name="Deniz"
surname="Somuncuoglu"
print("My name is {} {}".format(name,surname))

# str alternatif v1
print("My name is {0} {1}".format(name,surname))

# str alternatif v2
print("My name is {n} {s}".format(n=name,s=surname))


result=200/658
print("the result is {}".format(result))

# float alternatif v1
print("the result is {r:1.3}".format(r=result)) # r:virgülün sol tarafı, virgülün sağ tarafından sonra kaç sıfır olacağı

# all variables
print(f"My name is {name} {surname}") # Tırnaklardan önce 'f' gelirse

