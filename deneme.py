def fonksiyon():
    print("merhaba")
while True:
    cevabın=input("Ayanaya cevabını ilet ve sadece numaraları kullan")
    if(cevabın=="q"):
        print("Programdan Çıkılıyor...")
        time.sleep(3)
        break
    cevabın=int(cevabın)
    if (cevabın==1):
       fonksiyon()
    elif(cevabın==2):
        fonksiyon()