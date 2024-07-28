genc_sozluk = {
    "itidal": "soğukkanlı",
    "fiktif": "suni, yapay",
    "string": "karakterler listesi",
    "encoding": "bir karakterin bitler (0 ve 1) ile temsili"
}

yeni_terim = input("Eklemek İstediğin terim nedir")
yeni_anlam = input("Kelimenin anlamı nedir")

genc_sozluk[yeni_terim] = yeni_anlam

sorgu = input("Hangi kelimenin anlamını öğranmek istersin ?")
print(genc_sozluk[sorgu])
input