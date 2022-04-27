import random
import sys


def ogrenciarat(ogrenci,ogrencino,no):
    print("Aratmak istedigin ogrenci no gir")
    ogrencino=input()

    
    if(ogrencino not in no):
        return print("Ogrenci no bulunamamistir.")

    elif(ogrencino in no):
        sira=no.index(ogrencino)*6
        return print(ogrencino,"No'lu Ogrencinin adi", ogrenci[sira+1],", vizesi ",ogrenci[sira+2],", finali ",ogrenci[sira+3],
        ", basari puani ",ogrenci[sira+4],", basari notu ", ogrenci[sira+5]," seklindedir. ")
    
        
def Hesaplama(a,b) :

   return round((float(a)*(4/10) + float(b)*(6/10)),2)

def Harfnotu(sonuc) :

    if(sonuc >=94):
        return "A1" 
    elif(sonuc >=89):
        return "A2" 
    elif(sonuc >=84):
        return "A3"
    elif(sonuc >=79):
        return "B1"
    elif(sonuc >=74):
        return "B2"
    elif(sonuc >=69):
        return 'B3'
    elif(sonuc >=64):
        return'C1'
    elif(sonuc >=59):
        return 'C2'
    elif(sonuc >=54):
        return 'D1'
    elif(sonuc >=49):
        return'D2'
    elif(sonuc >=0):
        return 'FF'

def vize() :
    ogrenci=[]
    no=[]
    sayi=0
    while sayi!=10:
        print((sayi+1),". ogrencinin numarasini giriniz:") 
        ogrencino=input()
        no+=[ogrencino]

        print((sayi+1),". ogrencinin adini giriniz.(Cikis icin 0 giriniz):")
        ad=input()
        
        if ad=="0":
            sys.exit("Cikis yapilmistir.")
         
        
        
        vize1=(random.randint(0,100))

        Final=(random.randint(0,100))
        ort=Hesaplama(vize1,Final)
        
        ogrenci+=[no,ad,vize1,Final,Hesaplama(vize1,Final),Harfnotu(ort)]
        
        sayi+=1
    say=0
    bilgi=0
    while say!=10:

        print(say+1,". ogrenci",no[say],ogrenci[bilgi+1],ogrenci[bilgi+2],ogrenci[bilgi+3],ogrenci[bilgi+4],ogrenci[bilgi+5])
        say+=1
        bilgi+=6
    
    ogrenci==ogrenciarat(ogrenci,ogrencino,no)
def bitti():

    
    son=input("\nProgramin sonuna geldiniz. Cikis yapmak icin enter tusuna basiniz.")
    
   
vize()
bitti()





