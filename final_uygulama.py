import tkinter
from random import choice


class Simonderki() :
    def __init__(self, master):

        self.master = master
        self.master.minsize(480, 360) # Ekran çözünürlüğünü ayarlar.
        self.master.title("Simon Der Ki") # Oyun başlığı.
        self.master.update() # Anasayfanın yenilenmesini sağlar.

        # Canvas kodları oyuna temel şeklini vermemizi sağlar.
        self.simon_canvas = tkinter.Canvas(self.master, width=self.master.winfo_width(), height=self.master.winfo_height(), highlightthickness=5)
        self.simon_canvas.pack()

        # Oyunun renklerini ayarlıyoruz.
        self.ana_renkler = ("#ff0000", "#0066ff", "#00ff00", "#ffff00")
        self.parlak_renkler = ("black", "black", "black", "black")
        self.renkler = [color for color in self.ana_renkler]
        self.dikdortgenler = []

        # Kullanıcının renkleri doğru sırayla seçmesi için gerekli komutlar.
        self.sira = [choice(self.ana_renkler)]
        self.sira_yeri = 0
        self.canvas_ciz()
        self.sirayi_goster()
        self.master.mainloop()

        # Sıralamayı oyuncuya gösteriyoruz ki tekrarlayabilsin.
    def sirayi_goster(self):

        self.yakıpsondur(self.sira[self.sira_yeri]) # Sıradaki dikdörtgenin yanıp sönmesi için yukarıda numaralarını yazdığımız açık renklerin gelmesi gerekiyor.
        if(self.sira_yeri < len(self.sira) - 1):# Sıranın sonuna gelip gelmediğini sorgular.
            self.sira_yeri += 1 # Sıranın sonuna gelmediğimiz için (oyun devam ettiği için) 1 hamle daha ekler.
            self.master.after(1500, self.sirayi_goster) # Yanıp sönmeler arası 1,5 saniyleik gecikme ekler.
        else :
            self.sira_yeri = 0 # Eğer oyun bittiyse oyunu sıfırlar.

    def yakıpsondur(self, color):
        index = self.ana_renkler.index(color) # Tanımlama kısmında belirtilen renklerin yerini buldurur.
        if self.renkler[index] == self.ana_renkler[index] : # Yanıp sönen rengin doğru renk olup olmadığını konumunu kullanarak kontrol eder.
            self.renkler[index] = self.parlak_renkler[index]# Burada yanıp sönecek renk yukarıda belirtilen açık renge ayarlanır.
            self.master.after(1250, self.yakıpsondur, color) # Yanıp sönme süresini 1.25 saniye olarak ayarlar.
        else :
            self.renkler[index] = self.ana_renkler[index] # Yanıp sönerken gelen açık rengi terkar eski haline çevirir.
        self.canvas_ciz() # Değişikliği oyuncuya yansıtmamız için gerekli kod.


    def kontrol_choice(self):
        dikdortgen_kimligi = self.simon_canvas.find_withtag("current")[0]
        dikdortgen_index = self.dikdortgenler.index(dikdortgen_kimligi)
        color = self.ana_renkler[dikdortgen_index]
        if color == self.sira[self.sira_yeri]:
            if self.sira_yeri < len(self.sira) - 1:
                self.sira_yeri += 1
            else :
                self.master.title("Simon Der Ki - Skor: {}".format(len(self.sira))) # Skoru oyunun başlık kısmında hamle(sıra) sayısına göre günceller.
                self.sira.append(choice(self.ana_renkler))# Renkler doğru girildiğinde sonuna bir hamle daha ekler.
                self.sira_yeri = 0
                self.sirayi_goster()
        else :
            # Oyuncu yanlış hamle yaptığında oyunu en başa çevirir.
            self.master.title("Simon Der Ki  - Kaybettin! | Skorun: {}".format(len(self.sira))) #Oyun bittiğinde son skoru yapılan doğru hamle(sıra) sayısına göre verir.
            self.sira[:] = [] # Skoru sıra sayısına göre belirlediğimiz için oyun kaybedildiğinde sıra sayısını sıfılar.
            self.sira.append(choice(self.ana_renkler))# Oyun kaybedildiği için en baştan tekrar bir hamle gösterir.
            self.sira_yeri = 0
            self.sirayi_goster()

    def canvas_ciz(self):
        self.dikdortgenler[:] = [] # Dikdörtgenler listesini boşaltır.
        self.simon_canvas.delete("all") # Canvas katmanını temizler.
        for index, color in enumerate(self.renkler): # Listedeki renkler üzerinde dikdörtgenlerin her birinin kendi yerlerini çizerek yineler.
            if index <= 1:
                rectangle = self.simon_canvas.create_rectangle(
                                          index * self.master.winfo_width(),
                                          0, self.master.winfo_width() / 2,
                                          self.master.winfo_height() / 2,
                                          fill = color, outline = color)
            else:
                rectangle = self.simon_canvas.create_rectangle(
                                        (index - 2) * self.master.winfo_width(),
                                        self.master.winfo_height(),
                                        self.master.winfo_width() / 2,
                                        self.master.winfo_height() / 2,
                                        fill = color, outline = color)
            self.dikdortgenler.append(rectangle)
        for id in self.dikdortgenler:
            self.simon_canvas.tag_bind(id, '<ButtonPress-1>', lambda e : self.kontrol_choice()) # Tıkladığımızda tuşun çalışmasını sağlar.

def main():
    root = tkinter.Tk()
    gui = Simonderki(root)

if __name__ == "__main__" : main()
