from tkinter import *
from PIL import ImageTk, Image

class kutuphane:

    def __init__(self,anasayfa):
        global pano, message
        self.anasayfa = anasayfa
        anasayfa.title = ("Kütüphane Kataloğu")
        anasayfa.configure(background="black")
        root.wm_iconbitmap("katalogsimge.ico")

        self.fotograf = Image.open("hacettepe_logo_.png")
        self.tkimage = ImageTk.PhotoImage(self.fotograf)
        self.hacettepelogo = Label(anasayfa, image=self.tkimage)
        self.hacettepelogo.grid(column=1)
        Label(anasayfa, bg="red").grid(column=1, row=1)

        self.kitap_ekle = Button(anasayfa, text="Kitap Ekle", bg="black",fg="red",font = "bold", command = self.kitap_ekle)
        self.kitap_ekle.grid(column=1, row=1)

        self.kitapları_listele = Button(anasayfa, text="Kitapları Listele", bg="black", fg="red", font="bold", command= self.listele)
        self.kitapları_listele.grid(column=1,row=2)

        self.cikis = Button(anasayfa, text="Kapat", command=exit, fg="red", bg="black", font="bold")
        self.cikis.grid(column=1, row="6")

    def kitap_ekle(self):
        global kitap_adi, yazar_adi, tur, isbn, yayinevi, yayin_yili, kitapbak #global yazmazsak çalışmıyor.
        eklemepencere = Tk()
        eklemepencere.wm_iconbitmap("katalogsimge.ico")
        eklemepencere.geometry("250x220")
        pencerebaslik = eklemepencere.title("Kitap Ekle")
        eklemepencere.configure(background="black")
        kitap_adi = Entry(eklemepencere)
        yazar_adi = Entry(eklemepencere)
        tur = Entry(eklemepencere)
        isbn = Entry(eklemepencere)
        yayinevi = Entry(eklemepencere)
        yayin_yili = Entry(eklemepencere)

        kitap_adi.grid(column=2, row=2)
        yazar_adi.grid(column=2, row=3)
        tur.grid(column=2,row=4)
        isbn.grid(column=2,row=5)
        yayinevi.grid(column=2,row=6)
        yayin_yili.grid(column=2,row=7)

        Label(eklemepencere, font = "bold", bg="black", text='Kitap Ekle', fg= "red").grid(column=2, row=1)
        Label(eklemepencere, font = "bold", bg="black", text='Kitap Adı :', fg= "red").grid(column=1, row=2,)
        Label(eklemepencere, font = "bold", bg="black", text='Yazar Adı :', fg= "red").grid(column=1, row=3,)
        Label(eklemepencere, font = "bold", bg="black", text='Kitabın Türü :', fg= "red").grid(column=1, row=4)
        Label(eklemepencere, font = "bold", bg="black", text='ISBN :', fg="red").grid(column=1, row=5)
        Label(eklemepencere, font = "bold", bg="black", text='Yayınevi :', fg="red").grid(column=1, row=6)
        Label(eklemepencere, font = "bold", bg="black", text='Yayın Yılı :', fg="red").grid(column=1, row=7)

        self.exit = Button(eklemepencere, bg="black", text="Kapat", font="bold", fg="red", command=eklemepencere.destroy)
        self.exit.grid(column=1, row=8)
        self.kaydet = Button(eklemepencere, bg="black", text="Kaydet", font="bold", fg="red", command=self.kaydet)
        self.kaydet.grid(column=2, row=8)

    def kaydet(self):
        kaydedilecekbilgiler = ["****  " + "Kitap Adı: "+ kitap_adi.get()+ " | "+ "Yazarı: " + yazar_adi.get()+ " | "+ "Türü: " + tur.get()+ " | "+ "ISBN: " + isbn.get()+ " | "+ "Yayınevi: " + yayinevi.get()+ " | "+ "Yayın Yılı: " + yayin_yili.get()+ "  ****"+ "\n"]
        f = open("kitaplistesi.txt", 'a')
        for i in kaydedilecekbilgiler:
            f.write(i)
        f.close()

    def listele(self):
        liste = Tk()

        file = open("kitaplistesi.txt")
        data = file.read()
        file.close()
        kitap_liste = Label(liste, text=data, bg="black", fg ="red")
        kitap_liste.grid(row=1, column=2)
        self.exit = Button(liste, bg="black", text="Kapat", font="bold", fg="red",  command=liste.destroy)
        self.exit.grid(column=2, row=3)

        pencerebaslik = liste.title("Kitap Listesi")
        liste.configure(background="black")


root = Tk()
kutuphanem = kutuphane(root)
root.mainloop()
