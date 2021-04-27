import string

def vynasob(a, b):
    a = a.replace(",", ".")
    print (a)
    return float(a) * b

a = "23,8"
b = 6
print(vynasob(a, b))
