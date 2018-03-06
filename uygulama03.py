__author__ = "Serhat ARSLAN" #06.03.2018
#Liste ve Sözlük kullanarak basit bir inglizce-türkçe renkler sözlüğü.
Colors = ["Red", "Orange", "Brown", "Yellow", "Green", "Turquoise", "Blue", "Purple", "Pink", "White", "Grey", "Black"  ]
print(Colors)
print("*"*110)
Colors_dict = {"Red": "Kırmızı", "Orange": "Turuncu", "Brown": "Kahverengi", "Yellow": "Sarı", "Green": "Yeşil", "Turquoise": "Turkuaz", "Blue": "Mavi", "Purple": "Mor", "Pink": "Pembe", "White": "Beyaz", "Grey":"Gri", "Black":"Siyah" }

print(Colors_dict [input("Türkçesini görmek istediğiniz rengi yazın(ilk harf büyük):")])
print("*"*110)