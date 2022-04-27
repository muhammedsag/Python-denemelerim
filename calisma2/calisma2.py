import random
import time
import sys

#1.soru----------------------------------------------------------------------------------------------------------------------
def tekcift(baslangic,bitis) :
    #print("Hangi sayiya kadar cift tek hesaplayalım ?")
    #baslangic=int(input("Baslangicini giriniz: "))
    #bitis=int(input("Bitisi giriniz: "))
    carpim=[]
    my_list = range(baslangic, bitis)
    tekler = list(filter(lambda varX: varX % 2 == 1, my_list))
    random.shuffle(tekler)
    result=tekler
    print("Tek sayi listesi  : ",result)


    my_list2 = range(baslangic, bitis)
    ciftler=list(filter(lambda varX: varX %2 == 0,my_list2))
    random.shuffle(ciftler)
    result2=ciftler
    print("Cift sayi listesi : ",result2)

    listetoplam= tekler+ciftler
    print("\nTek sayi listeniz ile cift sayi listenizin toplami bu sekildedir: ",listetoplam)
    
   
    index=0
    while baslangic!=bitis:
        carpim+=[listetoplam[index]*2]
        #print(listetoplam[i]*2)
        baslangic+=1   
        index+=1 
    print("\nTek ve Cift sayilarinizin 2 kati                                : ",carpim,"budur.")

tekcift(0,10)


#2.soru-----------------------------------------------------------------------------------------------------------------------
#a)
def firma(id):
    time.sleep(1)
    print(id,"no'lu ID aratiliyor... Lutfen bekleyiniz.")
    time.sleep(1)

    aday1= {"Adi": "Ayşe yılmaz",
    "meslek":"endüstri mühendisi",
    "numara":"05543567887",
    "yaş":"24",
    "ingilizce bilgisi":"çok iyi"}
    aday2= {"Adi": "mehmet kaymaz ",
    "meslek":"bilgisayar mühendisi",
    "numara":"05387986655",
    "yaş":"29",
    "ingilizce bilgisi":"iyi"}
    aday3= {"Adi": "hikmet acar",
    "meslek":"bilgisayar mühendisi",
    "numara":"05312459087",
    "yaş":"32",
    "ingilizce bilgisi":"çok iyi"}
    aday4= {"Adi": "selin parlak",
    "meslek":"yazılım mühendisi",
    "numara":"05376665434",
    "yaş":"26",
    "ingilizce bilgisi":"iyi"}
    aday5= {"Adi": "hakan adıgüzel",
    "meslek":"endüstri mühendisi",
    "numara":"05678907744",
    "yaş":"30",
    "ingilizce bilgisi":"orta"}

    #b
    toplam={
            1:aday1,
            2:aday2,
            3:aday3,
            4:aday4,
            5:aday5
            }
    #c
    print(toplam.get(id,"Aradığınız ID adaylar arasinda bulunamamistir.")) 

    #id= input("id no giriniz:")
    #if (id in toplam):
     #   print("{} id numaralı adayın bilgileri:".format(id))
      #  print(toplam[id])
    #elif (id not in toplam):
     #   print("Adayin id'si bulunamamistir. ")

firma(1)


#3.soru--------------------------------------------------------------------------------------------------------------------------

def buyukkücük():

    metin =input("Verilen ifade: ")
    upper=0
    lower=0
    for i in metin:
        if (i.islower()):
            lower=lower+1
        elif (i.isupper()):
            upper=upper+1
    print("Verilen ifadede bulunan büyük harflerin sayısı:",upper)
    print("Verilen ifadede bulunan küçük harflerin sayısı:",lower)


buyukkücük()



def bitti():
    a=input("Program bitti.")
    sys.exit

bitti()





