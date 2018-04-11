__author__ = "Serhat ARSLAN"

import random
kelime_havuzu = random.choice(["plüton", "neptün", "uranüs", "jüpiter", "satürn", "merkür", "venüs", "mars", "dünya"])
kalan_can = 6
pano = []
alt_tire = "_"
print("Adam Asmaca oyununa hoşgeldiniz..\n")
for kelime in kelime_havuzu:
    pano.append(alt_tire)
print(pano)
while kalan_can > 0:
    i = 0
    alinan_harf = input("\nBir harf tahmin edin: ").lower()
    if alinan_harf in kelime_havuzu:
        for kontrol in kelime_havuzu:
            if kelime_havuzu[i] == alinan_harf:
                pano[i] = alinan_harf
            i += 1
        print("")
        print(pano)
        print("\n Doğru tahmin! ")
    else:
        kalan_can -= 1
        print("")
        print(pano)
        print("\n Yanlış tahmin!")
        print("\nKalan can = %s" %kalan_can)
    if kalan_can == 0:
        print("Öldün çık! Doğru cevap: %s" %kelime_havuzu)
        break
    if alt_tire not in pano:
        print("\nKazandın!")
        break
