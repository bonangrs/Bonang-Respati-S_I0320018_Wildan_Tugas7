judul = "Menghitung persentase huruf dalam sebuah kalimat"
print(judul.upper().center(60, '='))

kalimat = input("Masukkan kalimat: ")
huruf = input("Masukkan huruf: ")

if len(huruf) > 1:
    print("Mohon masukkan 1 huruf")
elif huruf.isalpha() is False:
    print("Huruf tidak terdeteksi")
else:
    jmlh = kalimat.upper().count(huruf.upper())
    persen = (jmlh / len(kalimat)) * 100
    print('Terdapat {} huruf "{}" dalam kalimat "{}"'.format(jmlh, huruf, kalimat))
    print('Kalimat "{}" mengandung {}% huruf "{}"'.format(kalimat, round(persen, 2), huruf))
