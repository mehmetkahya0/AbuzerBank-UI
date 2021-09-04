print("""
AbuzerBank UI Tkinter!
480 Satır


--Yazılma Tarihleri: 29.08.2021 - 30.08.2021 - 1.09.2021 - 

|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
    Eklenen Özellikler; 
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
        29.08.2021: Ana temel oluşturuldu, Hesap girme kısmı yapıldı, Hesap detayları yapıldı 
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
        30.08.2021: Kayıt olma eklendi, Kayıt UI oluşturuldu, Anlık console takip eklendi, para çekme ve kalan bakiye eklendi, 
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
        1.09.2021: Kredi çekme ekledi ve hesap işlemleri algoritmaları yenilendi, admin paneli bitti, kredi şartları eklendi, para gönderme eklendi, 
            para gönderimine filtreler eklendi, Hata kodları listelendi
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
        4.09.2021: Destek kısmı terminale taşınıdı, destek dili ingilizceye çevrildi(terminal bazen türkçe karakterlerde hata verdi), proje son halini aldı.
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|



""")

from tkinter import *
import tkinter as tk
from tkinter import ttk
import time
import random
import math

pencere = tk.Tk(className='AbuzerBank')
pencere.geometry('500x500+700+200')
pencere.configure(bg="dark grey")

name_var=tk.StringVar()
passw_var=tk.StringVar()
para =tk.IntVar()
para_cek=tk.IntVar()
bakiye = tk.IntVar()
kalan = tk.IntVar()
kredi =tk.IntVar()
kredi_cek=tk.IntVar()
para_miktar = tk.IntVar()
gonderilen_p = tk.IntVar()
parag = tk.IntVar()

kullanıcılar = ["Mehmet123","mehmet","ege","Abuzer"]
sifreler = ["123","321","1","2","3","4","0000"]
base = {
  "Mehmet123": 123,
  "Abuzer": 0000,
  "ege": 2012
}

label3=Label(pencere)
label8=Label(pencere)
label9=Label(pencere)
label10 = Label(pencere)
label11 = Label(pencere)
label12 = Label(pencere)
label13 = Label(pencere)
label14 = Label(pencere)
entry3 = Entry(pencere)
entry4 = Entry(pencere)
buton4 = Button(pencere)
buton5 = Button(pencere)
entry5 = Entry(pencere)
label15 = Label(pencere)
buton6 = Button(pencere)
label16 = Label(pencere)
checkvar1 = IntVar()  
buton7 = Button(pencere)
label17 = Label(pencere)
label18 = Label(pencere)
label19 = Label(pencere)
label20 = Label(pencere)
label21 = Label(pencere)
buton8 = Button(pencere)
label22 = Label(pencere)
label23 = Label(pencere)
label24 = Label(pencere)
label25 = Label(pencere)
entry6 = Entry(pencere)
label26= Label(pencere)
label27 = Label(pencere)
label28 = Label(pencere)
label29 = Label(pencere)
label30 = Label(pencere)
label31 = Label(pencere)
label32 = Label(pencere)
label33 = Label(pencere)
label34 = Label(pencere)
label35 = Label(pencere)
entry7 = Entry(pencere)
entry8 = Entry(pencere, show = "*")
buton9 = Button(pencere)
label36 = Label(pencere)
entry9 = Entry(pencere)
label37 = Label(pencere)
buton10 = Button(pencere)

bakiye = int(random.randint(2000, 10000))
yas = random.randint(18,100)

def checkvar2():
    print("Gizlilik Sözleşmesi Onaylandı!")


#destek
def destek():

    destek = str(input("[help], [system shutdown], [Users], [Passwords] : "))

    if destek == "help":
        print(""" 
        ################################################
        ##               HATA KODLARI                 ##
        ################################################
        #| 0001 = Kullanıcı adı veya şifre yanlış     |#
        #|---------------------------------------     |#
        #| 0002 = Kredi için min. miktardan az bakiye |#
        #|--------------------------------------------|#
        #| 0003 = Bakiyeden Fazla Para Çekmek         |#
        #|--------------------------------------------|#
        #| 0004 = Hatalı Şifre                        |#
        #|--------------------------------------------|#
        #| 0005 = Hatalı Kullanıcı Adı                |#
        #|--------------------------------------------|#
        #| 0006 = Para gönderme limitinden az bakiye  |#
        #|--------------------------------------------|#
        #| 0007 - Bakiyeden Fazla Para Gönderme İsteği|#
        ################################################""")

    if destek == "system shutdown":
        print("System Shutdown -activated")
        time.sleep(0.5)
        exit()

    if destek == "Users":
        print(kullanıcılar)

    if destek == "Passwords":
        print(sifreler)

#para gönderme
def para_gonder():

    kullanıcı2 = entry7.get()
    sifre2 = entry8.get()

    print("para gönderme - online")

    if kullanıcı2 in kullanıcılar:   
        print("Kullanıcı Adı Bulundu!") 
    else:
        print("HATA KODU: 0005")
        print("para gönderme - deactivated")
        exit()
    if sifre2 in sifreler:   
        print("Şifre Bulundu!")

    else:
        print("HATA KODU: 0004")
        print("para gönderme - deactivated")
        exit()


    para_gonder = parag.get()
    parag.set("")

    if bakiye > 50:
        print(bakiye+para_gonder)

        print("\n Para gönder -activated")
        print("\n Gönderilen Miktar: ")
        print(para_gonder)
        total = (bakiye-para_gonder)
        print("Kalan Bakiye: {}".format(total))
        label26 = Label( pencere,text="Kalan Bakiye: {} ".format(total), textvariable=total, relief=RAISED, fg="red")
        label26.place(x=121,y=412)

    else:
        print("\n para gönder -deactivetad")
        print("Para gönderme için yetersiz bakiye")
        label27 = Label( pencere,text="HATA KODU 0006",relief=RAISED )
        label27.place(x=320,y=200)
        exit()

    if para_gonder > bakiye:
        print("Bakiyeden fazla gönderim isteği!")
        label37 = Label( pencere,text="HATA KODU 0007",relief=RAISED )
        label37.place(x=121,y=412)

#Kredi çekme algoritma
def kredi_al():

    kredi_cek = kredi.get()
    kredi.set("")
    if bakiye > 5000:
        print(bakiye+kredi_cek)
        print("Hesap Bekiyesi 5000₺ den fazla, Kredi çekmek için uygun")
        print("\n Kredi -activated")
        print("\n Çekilen Kredi: ")
        print(kredi_cek)
        total = (bakiye+kredi_cek)
        print("Toplam Bakiye: {}".format(total))
        label26 = Label( pencere,text="Toplam Bakiye: {} ".format(total), textvariable=total, relief=RAISED )
        label26.place(x=320,y=200)

    else:
        print("\n Kredi -deactivetad")
        print("Kredi için yetersiz bakiye")
        label27 = Label( pencere,text="HATA KODU 0002",relief=RAISED )
        label27.place(x=320,y=200)


#Para çekme algoritma
def cekilen_para():

    para_cek = para.get()
    para.set("")

    if para_cek > bakiye:
        kod = print("Hata Kodu 0002")
 #      label16 =  Label(pencere,textvariable = kalan, font=('calibre',10,'normal'))  
        label16 = Label( pencere,text="Hata Kodu 0002".format(kod), relief=RAISED )
        label16.place(x=320,y=151)

    if para_cek < bakiye:
        print("Çekilen Para: ")
        print(para_cek)
        kalan = (bakiye-para_cek)
        print("Kalan Bakiye: {}".format(kalan))
 #       label16 =  Label(pencere,textvariable = kalan, font=('calibre',10,'normal'))  

        label16 = Label( pencere,text="Kalan Bakiye:{} ".format(kalan), textvariable=kalan, relief=RAISED )
        label16.place(x=320,y=151)


def cıkıs():
    print("Çıkış Yapıldı! -system out")
    exit()


def after_sign():

    name= name_var.get()
    password = passw_var.get()

    print("Kullanıcı adı: "+ name)
    print("Şifre: "+ password)
    
    name_var.set("")
    passw_var.set("")

    label14.config(text="Kayıt Başarılı Çıkış Yapın.",bg="dark grey",fg="dark red")
    print("{} Kaydı Başarıyla Oluşturuldu!".format(name))
    label14.place(x=109,y=285)


def sign_up():
    print("Kayıt ol! -activated ")

    entry1.destroy()
    buton1.destroy()
    entry2.destroy()
    label6.destroy()
    label7.destroy()
    buton2.destroy()
    label2.destroy()
    label.destroy()
    buton7.destroy()
    label10.config(text="Kayıt ol",font=("Impact",30),bg="dark grey")
    label10.place(x=20,y=20)



  #  entry3 = Entry(pencere)
   # entry3.place(x=110,y=100)

    label11.config(text=("Kullanıcı Adı:"),bg="dark grey")
    label11.place(x=10,y=101.2)

    label12.config(text=("Şifre:"),bg="dark grey")
    label12.place(x=60,y=150)

#entry4 = Entry(pencere)
#entry4.place(x=110,y=150)

    entry3 =  Entry(pencere,textvariable = name_var, font=('calibre',10,'normal'))   
    entry3.place(x=110,y=100)

    entry4= Entry(pencere, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
    entry4.place(x=110,y=150)

    buton4 = Button(pencere)
    buton4.config(text="Kayıt ol",bg="dark grey",fg="black",command = after_sign)
    buton4.place(x=160,y=210)  
    
    buton5.config(text="Çıkış",bg="dark grey",fg="dark red",command = cıkıs)
    buton5.place(x=168,y=267) 
#checkbutton
    chkbtn1 = Checkbutton(pencere, text = "Gizlilik", variable = checkvar1,command=checkvar2 ,onvalue = 1, offvalue = 0,height = 1, width = 10)  
    chkbtn1.pack(side="left",padx=135)  

def sign_in():

    kullanıcı = entry1.get()
    sifre = entry2.get()

    if kullanıcı in kullanıcılar:   
        print("Kullanıcı Adı Doğru!") 

    if sifre in sifreler:   
        print("Şifre Doğru!") 

    else:
        print("HATA KODU: 0001")
        exit()

#Hesap Kısmı 
    label2.destroy()
    time.sleep(0.5)
    label.config(text="AbuzerBank'a Hoşgeldin {}!".format(kullanıcı))
    label.place(x=20,y=20)

    entry1.destroy()
    buton1.destroy()
    entry2.destroy()
    label6.destroy()
    label7.destroy()
    buton2.destroy()
    buton7.destroy()

    print("{} Sisteme Girdi!".format(kullanıcı))

    time.sleep(0.5)
    label3.config(text="İsim: {}".format(kullanıcı),font=("DIN Condensed",20),bg="dark grey")
    label3.place(x=20,y=58)

    label8.config(text="Bakiye: {}".format(bakiye),font=("DIN Condensed",20),bg="dark grey")
    label8.place(x=20,y=83)

    label9.config(text="Yaş: {}".format(yas),font=("DIN Condensed",20),bg="dark grey")
    label9.place(x=20,y=108)

    label15.config(text="Para Çek:",font=("DIN Condensed",15),bg="dark grey")
    label15.place(x=23,y=150)

    entry5 = Entry(pencere,textvariable = para, font=('calibre',10,'normal'))   
    entry5.place(x=100,y=150)
 
    buton6.config(text="Onayla",bg="dark grey",fg="black",command=cekilen_para)
    buton6.place(x=260,y=151)

    label25.config(text="Kredi Çek:",font=("DIN Condensed",15),bg="dark grey")
    label25.place(x=23,y=200)

    entry6 = Entry(pencere,textvariable = kredi, font=('calibre',10,'normal'))   
    entry6.place(x=100,y=200)
    
    buton8.config(text="Onayla",bg="dark grey",fg="black",command=kredi_al)
    buton8.place(x=260,y=201)

    label35.config(text="Para Gönder:",font=("DIN Condensed",20),bg="dark grey")
    label35.place(x=23,y=270)

    label33.config(text="İsim:",font=("DIN Condensed",15),bg="dark grey")
    label33.place(x=23,y=303)
  
    #entry7 = Entry(pencere,font=('calibre',10,'normal'))   
    #entry7.place(x=100,y=300)
    
    label34.config(text="Numara:",font=("DIN Condensed",15),bg="dark grey")
    label34.place(x=23,y=330)

   # entry8 = Entry(pencere, font=('calibre',10,'normal'))   
  #  entry8.place(x=100,y=330)

    buton9.config(text="Gönderimi Onayla",bg="dark grey",fg="black",command=para_gonder)
    buton9.place(x=128,y=387)

    entry7.place(x=100,y=300)
    entry8.place(x=100,y=330)

    
    label36.config(text="Miktar:",font=("DIN Condensed",15),bg="dark grey")
    label36.place(x=23,y=360)

    entry9 =  Entry(pencere,textvariable = parag, font=('calibre',10,'normal'))   
    entry9.place(x=110,y=360)

#Admin Paneli
def admin():
    print("Admin Paneli giriş -activated")
    son = random.randint(100,500)
    toplam = random.randint(1000, 1000000)
    label.destroy()
    entry1.destroy()
    buton1.destroy()
    entry2.destroy()
    label6.destroy()
    label7.destroy()
    buton2.destroy()
    buton7.destroy()


    label17.config(text="Admin Paneli:",font=("DIN Condensed",25),bg="dark grey")
    label17.place(x=20,y=45)

    label30.config(text="Admin Kullanıcı Adı:",font=("DIN Condensed",25),bg="dark grey")
    label30.place(x=20,y=45)


    label31.config(text="Admin Kullanıcı Adı:",font=("DIN Condensed",25),bg="dark grey")
    label31.place(x=20,y=45)

   
    label18.config(text="Mehmet!",font=("DIN Condensed",25),bg="dark grey")
    label18.place(x=200,y=45)

    label19.config(text="Bakiyeniz: 100.000.000.000$",font=("DIN Condensed",20),bg="dark grey")
    label19.place(x=20,y=110)
   
    label20.config(text="Adminlik Numarası: 00001",font=("DIN Condensed",20),bg="dark grey")
    label20.place(x=20,y=150)

    label21.config(text="Bugün gelen yeni kullanıcılar: {}".format(son),font=("DIN Condensed",20),bg="dark grey")
    label21.place(x=20,y=190)

    label22.config(text="Bugün bankaya yatırılan toplam para: {}".format(toplam),font=("DIN Condensed",20),bg="dark grey")
    label22.place(x=20,y=230)

    label23.config(text="Bugünkü Dolar Kuru: 8,30₺",font=("DIN Condensed",20),bg="dark grey")
    label23.place(x=20,y=270)

    label24.config(text="Bugünkü Euro Kuru: 9,84₺",font=("DIN Condensed",20),bg="dark grey")
    label24.place(x=20,y=310)

label=Label(pencere)
label.config(text="Hesap Girişi:",font=("DIN Condensed",25),bg="dark grey")
label.place(x=20,y=45)
   
label2=Label(pencere)
label2.config(text="AbuzerBank®",font=("Impact",20),bg="dark grey")
label2.place(x=20,y=18)

buton1 = Button(pencere)
buton1.config(text="Giriş yap",bg="dark grey",fg="black",command=sign_in, height=1, width=10)
buton1.place(x=180,y=208)

buton2 = Button(pencere)
buton2.config(text="Kayıt ol",bg="dark grey",fg="dark red",command=sign_up,height=1, width=10)
buton2.place(x=180,y=238)

buton7.config(text="Admin Girişi",bg="dark grey",fg="dark red",command=admin,height=1, width=10)
buton7.place(x=180,y=268)

label6=Label(pencere)
label6.config(text="Kullanıcı Adı: ",font=("Arial",15),bg="dark grey")
label6.place(x=26,y=101)

label7=Label(pencere)
label7.config(text="Şifre: ",font=("Arial",15),bg="dark grey")
label7.place(x=80,y=151)

entry1 = Entry(pencere)
entry1.place(x=130,y=100)


entry2 = Entry(pencere, show = "*")
entry2.place(x=130,y=150)


buton10.config(text="Destek [Terminal]",fg="dark red",bg = "dark grey",command=destek,height=1, width=12,borderwidth = 8)
buton10.place(x=15,y=475)


label28.config(text="2021 AbuzerBank® Tüm Hakları Saklıdır - Mehmet Kahya",font=("Arial",8),bg="dark grey")
label28.place(x=150,y=480)

mainloop()