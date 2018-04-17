_author_ = "Serhat ARSLAN" # 17.04.2018

import random
from tkinter import *
class uygulama:
    def __init__(self, master):
        self.master = master
        master.title ("UYGULAMA06")

        self.label = Label(master, text = "Günün Sözü", font = ("Arial", 14 ))
        self.label.pack()

        self.günün_sözü = Button(master, text = "♛ Günün Sözünü Gör ♛", font = ("Arial", 12), command=self.söz)
        self.günün_sözü.pack()

        self.çıkış = Button(master, text = "ஐ Çıkış ஐ", font = ("Arial", 12 ), command=master.quit)
        self.çıkış.pack(side="bottom")
    def söz(self):
        sözler = ("\nEn iyiyi bulmak için uğraşırken iyiyi kaybediyorsunuz. ☛ Shakespare", "\nİnsan coşkunluk anlarında olabildiğince bencildir. O dakikada kendisinden daha ilginç daha çekici bir konu olabileceğini düşünmez dünyada. ☛ Tolstoy", "\nHayat seni güldürmüyorsa, Espriyi anlamadın demektir. ☛ Anton Çehov", "\nMutlu olmak istiyorsan, bir amaca bağlan; insanlara ya da eşyalara değil. ☛ Albert Einstein", "\nTakdir ediliyorsan değil, Taklit ediliyorsan başarmışsın demektir. ☛ Albert Einstein", "\n Eğer onur kazançlı olsayԁı herkes onurlu olabilirdi. ☛ Thomas More", "\nİnsanın kinden kurtulması en yüksek umuda götüren köprü ve uzun süren kötü havalardan sonra görülen gökkuşağıdır. ☛ Friedrich Nietzsche", "\nAkılsızlar hırsızların en zararlılarıdır. Zamanınızı ve neşenizi çalarlar. ☛ Johann Wolfgang von Goethe", "\nCesaret de aşk gibi ümitle beslenir. ☛ Napoléon Bonaparte", "\nİçinde yaşanılan an, geleceği kemiren geçmiştir. ☛ Henri Bergson", "\nHak birilerinin size vereceği bir şey değil, hiç kimsenin sizden alamadığı bir şeydir. ☛ Ramsey Clark", "\nHer insan kendi görüş alanının sınırlarını, dünyanın sınırları olarak algılar. ☛ Arthur Schopenhauer", "\nZamanını hep engel aramakla geçirme. Belki de hiç engel yoktur. ☛ Franz Kafka", "\nKuşlar gibi uçmayı, balıklar gibi yüzmeyi öğrendik, ancak kardeşçe yaşamayı unuttuk. ☛ Martin Luther King", "\nYanlış düşün bu sorun değil. Ama her zaman kendin düşün. ☛ Gotthold Ephraim Lessing", "\nEğer onur kazançlı olsaydı, herkes onurlu olabilirdi. ☛ Thomas More", "\nBaşarı kolay elde edilir. Zor olan başarıyı hak etmektir. ☛ Albert Camus", "\nMutluluk erdemin ödülü değil erdemin kendisidir. ☛ Baruch Spinoza", "\nKötülüklerin ilki ve en büyüğü, haksızlıkların cezasız kalmasıdır. ☛ Platon", "\nGüç insanı yoldan çıkartır; mutlak güç ise insanı tamamen sapıttırır. ☛ Lord Acton" )

        seçilensöz = random.choice(sözler)
        self.bugününsözü = Label (self.master, text = seçilensöz)
        self.bugününsözü.pack()


root = Tk()
my_gui = uygulama(root)
root.mainloop()




