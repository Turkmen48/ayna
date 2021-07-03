#random ile her agresif,mutlu,normal durum için 5 farklı cümleyi random söylesin
#eğer toplam 0'dan küçükse agresif eşit ve büyükse iyiser cevaplar versin
#bir değişken daha olsun ilgi alanını bulucu eğer bilimsel şeyleri seçiyorsa bir konu söyle dediğinde bilimsel başka şeylerse onlar hakkında açsın
import time
import random
class sorular():
    def soru1():
        global toplam
        toplam=0
        soru=input("Çok konuşan ve boş konuşan insanlara tepkin nedir?\na-)Duymamazlıktan gelirim\nb-)Tahammül edemediğimi belli ederim\nc-)Sus artık tipini s....")
        if (soru=="a"):
            print("Cevabınız işleniyor...")
            time.sleep(3)
            toplam+=1
        elif(soru=="b"):
            print("Cevabınız işleniyor...")
            time.sleep(3)
            toplam+=0
        elif(soru=="c"):
            print("Cevabınız işleniyor...")
            time.sleep(3)
            toplam-=1
        else:
            print("""
            **********
            Lütfen a,b veya c şıklarından birini yazınız.
            **********
            """)
            return sorular.soru1()

    def soru2():
        global toplam
        soru=input("Sen çok sinirlendikten sonra karşı tarafın ne yapmasını beklersin?\na-)Bir şey beklemem gerekirse ben özür diler barışırım\nb-)Tane tane açıklama yapmalı\nc-)Özür dilemeli ve haklı olduğumu kabul etmeli")
        if (soru=="a"):
            print("Cevabınız işleniyor...")
            time.sleep(3)
            toplam+=1
        elif(soru=="b"):
            print("Cevabınız işleniyor...")
            time.sleep(3)
            toplam+=0
        elif(soru=="c"):
            print("Cevabınız işleniyor...")
            time.sleep(3)
            toplam-=1
        else:
            print("""
            **********
            Lütfen a,b veya c şıklarından birini yazınız.
            **********
            """)
            return sorular.soru2()
    def soru3():
        global toplam
        soru=input("Biriyle tartışmaya başladın ve ortam kızıştı ne yaparsın?\na-)Ortamı terk ederim\nb-)Bağırır çağırırım\nc-)Yumruk atarım ve kavgaya girerim")
        if (soru=="a"):
            print("Cevabınız işleniyor...")
            time.sleep(3)
            toplam+=1
        elif(soru=="b"):
            print("Cevabınız işleniyor...")
            time.sleep(3)
            toplam+=0
        elif(soru=="c"):
            print("Cevabınız işleniyor...")
            time.sleep(3)
            toplam-=1
        else:
            print("""
            **********
            Lütfen a,b veya c şıklarından birini yazınız.
            **********
            """)
            return sorular.soru3()
    def soru4():
        global ilgi_alani
        ilgi_alani = 0
        soru=input("Aşağıdaki haberlerden hangisi ilgini çeker?\na-)Sinir bilimi hakkında araştırma yapan bilim adamları yeni bir sempatik sinir buldu.\nb-)Recep Tayyip Erdoğan'ın Bahçeli hakkındaki şok sözleri!")
        if (soru=="a"):
            print("Cevabınız işleniyor...")
            time.sleep(3)
            ilgi_alani+=1
        elif(soru=="b"):
            print("Cevabınız işleniyor...")
            time.sleep(3)
            ilgi_alani-=1
        else:
            print("""
            **********
            Lütfen a,b veya c şıklarından birini yazınız.
            **********
            """)
            return sorular.soru4()
    def soru5():
        global ilgi_alani
        ilgi_alani = 0
        soru=input("Hangi konular ilgini çeker?\na-)Bilim/teknoloji\nb-)Magazin/eğlence")
        if (soru=="a"):
            print("Cevabınız işleniyor...")
            time.sleep(3)
            ilgi_alani+=1
        elif(soru=="b"):
            print("Cevabınız işleniyor...")
            time.sleep(3)
            ilgi_alani-=1
        else:
            print("""
            **********
            Lütfen a,b veya c şıklarından birini yazınız.
            **********
            """)
            return sorular.soru5()
    def soru6():
        global ilgi_alani
        ilgi_alani = 0
        soru=input("Youtube'de ne tür videolar izlersin?\na-)DIY(kendin yap),Oyun,Dizi\nb-)Müge Anlı,yemek tarifi,challenge,x kişisine şunu yaptım çok riskli oldu videoları.")
        if (soru=="a"):
            print("Cevabınız işleniyor...")
            time.sleep(3)
            ilgi_alani+=1
        elif(soru=="b"):
            print("Cevabınız işleniyor...")
            time.sleep(3)
            ilgi_alani-=1
        else:
            print("""
            **********
            Lütfen a,b veya c şıklarından birini yazınız.
            **********
            """)
            return sorular.soru6()
print("""
********************
AYNA'YA HOŞGELDİN
BU PROGRAM ALGORİTMASI İLE SENİ SİMÜLE EDECEKTİR
SENİ ANLAMAM İÇİN TESTİ BİTİR VE CEVAPLARI YAZARKEN HARFLERİ KULLAN (BÜYÜK/KÜÇÜK HARF DUYARLI!)
********************
""")

sorular.soru1()
sorular.soru2()
sorular.soru3()
sorular.soru4()
sorular.soru5()
sorular.soru6()
print("""
**********
AYNA OLUŞTURULUYOR...
**********
""")
time.sleep(3)
class cevaplar():
    def anla_merhaba():
        if(toplam<0):
            cevaplar.agresif_merhaba()
        elif(toplam==0):
            cevaplar.normal_merhaba()
        elif(toplam>0):
            cevaplar.iyi_niyetli_merhaba()
    def agresif_merhaba():
        liste=["Sen kime merhaba diyon lan?!","Selamun Aleykum","MERHABALAR AQ"]
        print(random.choice(liste))
    def normal_merhaba():
        liste=["Merhaba","(Sana cevap vermedi)","Merhabalar"]
        print(random.choice(liste))
    def iyi_niyetli_merhaba():
        liste=["MEERHAAABAAAA","Selam","Sana de merhaba canım"]
        print(random.choice(liste))
    def anla_nasilsin():
        if(toplam<0):
            cevaplar.agresif_nasilsin()
        elif(toplam==0):
            cevaplar.normal_nasilsin()
        elif(toplam>0):
            cevaplar.iyi_niyetli_nasilsin()
    def agresif_nasilsin():
        liste=["Sanane lan!","Ben iyiyim sen kendine bak babbbaa"]
        print(random.choice(liste))
    def normal_nasilsin():
        liste=["İyiyim","(Sana cevap vermedi)","İyiyim teşekkürler"]
        print(random.choice(liste))
    def iyi_niyetli_nasilsin():
        liste=["Ayyyy iyiyim teşekkürlerrr","İyii sen nasılsın? :)","Seni gördüm daha iyi oldum :)"]
        print(random.choice(liste))
    def anla_kavga():
        if(toplam<0):
            cevaplar.agresif_kavga()
        elif(toplam==0):
            cevaplar.normal_kavga()
        elif(toplam>0):
            cevaplar.iyi_niyetli_kavga()
    def agresif_kavga():
        liste=["DEMEK KAVGA İSTİYORSUN P*Ç GEL BURAYA(SANA 2 TANE ÇAKTI)","BÜYÜDÜNDE ADAM MI OLDUN LAN!","SANALDA ANA BACI REELDE ABİ BANA ACI İB*E TOP SENİ GEL BURAYA!"]
        print(random.choice(liste))
    def normal_kavga():
        liste=["Kardeşim git işine benimle uğraşma","(Sana karşılık vermedi)","La git diyom sana bana bulaşma"]
        print(random.choice(liste))
    def iyi_niyetli_kavga():
        liste=["Beyefendi kavgaya ne gerek var?","Bizim gibi medeni insanlara yakışmıyor lütfen!","(kaçtı)"]
        print(random.choice(liste))
    def anla_sev():
        if(toplam<0):
            cevaplar.agresif_sev()
        elif(toplam==0):
            cevaplar.normal_sev()
        elif(toplam>0):
            cevaplar.iyi_niyetli_sev()
    def agresif_sev():
        liste=["O ELİNİ ÇEK","O ELİNİ ALIRIM G*TUNE SOKARIM","S*KENİ SEVERLER, SEVENİ S*KERLER"]
        print(random.choice(liste))
    def normal_sev():
        liste=["Bunun ne için olduğunu bilmiyorum ama teşekkürler.","(O da sana sarıldı)"]
        print(random.choice(liste))
    def iyi_niyetli_sev():
        liste=["BENDE SENİ SEVİYORUMM!","Ayyy sen çok tatlısınnn!","(O sana daha sıkı sarıldı)"]
        print(random.choice(liste))
    def anla_ilgi_alani():
        if(ilgi_alani<=0):
            cevaplar.antibilimsel_ilgi_alani()
        elif(ilgi_alani>0):
            cevaplar.bilimsel_ilgi_alani()
    def bilimsel_ilgi_alani():
        liste=["Zaman makinesi yapılabilir mi?","Teknolojideki son gelişmeleri takip ediyor musun?","Plasebo etisi gerçek mi?","Sinir bilimi hakkında ne düşünüyorsun?","Yeni bir oyun çıkacak adı Death Stranding hiç duydun mu?",]
        print(random.choice(liste))
    def antibilimsel_ilgi_alani():
        liste=["Duydun mu yeniden seçime gidilebilirmiş...","Bu ekonomi çok iyi yağv yağğ?","Müge Anlı'da yapa ailesi katil çıktı ya aaaaa"]
        print(random.choice(liste))
print("""
*AYNA OLUŞTURULDU*

********************
1-) Aynaya "merhaba" de.
2-) Aynaya "nasılsın" de.
3-) Ayna ile kavga et.
4-) Ayna'yı sarıl.
5-) Ayna ilgi alanı hakkında bir konu seçsin.
********************
Çıkmak için "q" tuşuna bas
""")
while True:
    cevabın=input("Ayanaya cevabını ilet ve sadece numaraları kullan")
    if(cevabın=="q"):
        print("Programdan Çıkılıyor...")
        time.sleep(3)
        break
    cevabın=int(cevabın)
    if (cevabın==1):
        cevaplar.anla_merhaba()
    elif(cevabın==2):
        cevaplar.anla_nasilsin()
    elif(cevabın==3):
        cevaplar.anla_kavga()
    elif(cevabın==4):
        cevaplar.anla_sev()
    elif(cevabın==5):
        cevaplar.anla_ilgi_alani()
