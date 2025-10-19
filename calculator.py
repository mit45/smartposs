def topla(a,b):
    return a + b
def cikar(a,b):
    return a - b
def carp(a,b):
    return a * b
def bol(a,b):
    if b ==0:
        return "Bir sayı sıfıra bölünemez!"
    return a / b

print("Mini hesap makinesine hoşgeldiniz!")
print("İşlemler toplama, çıkarma, çarpma, bölme olarak tanımlanmıştır.")

islem = input("İşlem seç: ").lower()
sayi1 = float(input("Birinci sayıyı gir: "))
sayi2 = float(input("İkinci sayıyı gir: "))

if islem == "toplama":
    print("Sonuç:", topla(sayi1, sayi2))
elif islem == "çıkarma":
    print("Sonuç:", cikar(sayi1, sayi2))
elif islem == "çarpma":
    print("Sonuç:", carp(sayi1, sayi2))
elif islem == "bölme":
    print("Sonuç:", bol(sayi1, sayi2))
else:
    print("Geçersiz işlem seçildi.")