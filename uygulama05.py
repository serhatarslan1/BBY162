__author__ = "Serhat ARSLAN"

import random

bulunacakkelime = random.choice(["gitar", "piyano", "davul", "flüt", "keman", "org", "viyolonsel", "klarnet", "zurna", "trompet", "tuba", "bağlama"])

harfhavuzu = []

kalanhak = 6

altcizgi = "_"


gosterimyazisi = list(altcizgi * len(bulunacakkelime))

dongu = 1


while dongu:

    print(" ".join(gosterimyazisi),"\n") # Aralarında boşluk olacak şekilde kelimenin karakterlerini birleştiriyor.

    alinanharf = input("Bir harf tahmin edin: ").lower() # Büyük-küçük harf uyumluluğu için küçük harfe çevirdim.

    try: # try, input ile alınan verinin sayı olup olmadığını kontrol eder.
        int(alinanharf)
        print("Lütfen harf yazın.\n")
    except: # Except alınan harf 1 den uzun olduğunda hata mesajı verir.

        if len(alinanharf) > 1:
            print("Tek bir harf yazın.\n")
        else:

            if alinanharf in harfhavuzu:
                print("Bu harfi zaten girdiniz.\n")
            else:

                bulduk = None

                for i in range(len(bulunacakkelime)):
                    # kullanıcının girdiği harf, bulunucak kelimenin "i" nin taşıdığı sayı değerindeki indeksteki harfe eşit ise,
                    if alinanharf == bulunacakkelime[i]:

                        bulduk = True

                        gosterimyazisi[i] = alinanharf

                        harfhavuzu.append(alinanharf) # Alınan harf, harf havuzuna eklendi.

                        if altcizgi not in gosterimyazisi:

                            print(" ".join(gosterimyazisi)) # Aralarında boşluk olacak şekilde kelimenin karakterlerini birleştiriyor.
                            print("\nTebrikler kelimeyi buldun!")

                            dongu = 0
                            # Girilen harf aranan kelime içinde yoksa alttaki kodlar çalıştırılacak.
                else:

                    if bulduk != True:
                        kalanhak -= 1

                        print("Yanlış harf. Kalan hakkın: %s\n" %kalanhak)

                        harfhavuzu.append(alinanharf) # Alınan harf, harf havuzuna eklendi

                if kalanhak == 0:
                    print("Kaybettin! Doğru kelime =  %s  \n" %bulunacakkelime)

                    break