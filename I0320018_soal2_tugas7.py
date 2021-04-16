import math
print("====Menghitung luas dan sisi miring segitiga siku-siku====")


a = abs(float(input("Masukkan sisi alas: ")))
b = abs(float(input("Masukkan sisi tegak: ")))


def sisimiring(a, b):
    m = math.sqrt(a**2 + b**2)
    return round(m,2)


luas = a * b / 2
print("Sisi miring segitiga: {}".format(sisimiring(a,b)))
print("Luas segitiga: ", round(luas,2))

