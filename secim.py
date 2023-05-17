# Dosyayı aç ve verileri oku
#yorum
with open("oy.txt", mode='r', encoding= 'utf-8') as dosya:
    partiler = dosya.readline().strip().split(",")
    oy_orani = [float(x) for x in dosya.readline().strip().split(",")]
    oy_sayilari = [int(x) for x in dosya.readline().strip().split(",")]
    secilecek_temsilci_sayisi = int(dosya.readline().strip())
    ittifaklar = dosya.readline().strip().split(",")
    ortak_listeler = dosya.readline().strip().split(",")


# Oy oranlarını temsilci sayısına göre güncelle
sandalye = [0] * len(partiler)
while sum(sandalye) < secilecek_temsilci_sayisi:
    max_indeks = 0
    max_bolum = 0
    for i in range(len(partiler)):
        N = oy_sayilari[i] / (sandalye[i] + 1)
        if N > max_bolum:
            max_bolum = N
            max_indeks = i
    sandalye[max_indeks] += 1

# Ortak listeleri uygula
for transfer in ortak_listeler:
    kucuk_parti, buyuk_parti = transfer.split("->")
    kucuk_parti_indeksi = partiler.index(kucuk_parti)
    buyuk_parti_indeksi = partiler.index(buyuk_parti)
    sandalye[buyuk_parti_indeksi] += sandalye[kucuk_parti_indeksi]
    sandalye[kucuk_parti_indeksi] = 0

# İttifaklarda yer alan partilerin toplam temsilci sayılarını hesapla
ittifak_sandalyeleri = {}
for ittifak in ittifaklar:
    ittifak_partileri = ittifak.split("-")
    ittifak_sandalye_sayısı = sum([sandalye[partiler.index(parti)] for parti in ittifak_partileri])
    ittifak_sandalyeleri[ittifak] = ittifak_sandalye_sayısı

# Sonuçları ekrana yazdır
print("Parti Temsilci Sayıları:")
for i in range(len(partiler)):
    print(f"{partiler[i]}: {sandalye[i]}")

print("\nİttifak Temsilci Sayıları:")
for ittifak, koltuk_sayisi in ittifak_sandalyeleri.items():
    print(f"{ittifak}: {koltuk_sayisi}")
