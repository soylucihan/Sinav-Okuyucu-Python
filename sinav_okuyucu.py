

__author__ = "Cihan"
__date__ = "$06.Ara.2018 20:51:09$"

if __name__ == "__main__":
    
    
    anahtar=input("cevap nahtari gir \n")
    sozluk={}
    cevaplar={}
    puanlar={}
    sozluk["0"]="('"+input(" 1. ogrenci icin ad gir \n")+"','"+input(" 1. ogrenci icin soyad gir \n")+"')"
    cevaplar["0"]=input(" 1. ogrenci icin cevap gir \n")
    sozluk["1"]="('"+input(" 2. ogrenci icin ad gir \n")+"','"+input(" 2. ogrenci icin soyad gir \n")+"')"
    cevaplar["1"]=input(" 2. ogrenci icin cevap gir \n")
    sozluk["2"]="('"+input(" 3. ogrenci icin ad gir \n")+"','"+input(" 3. ogrenci icin soyad gir \n")+"')"
    cevaplar["2"]=input(" 3. ogrenci icin cevap gir \n")
    sozluk["3"]="('"+input(" 4. ogrenci icin ad gir \n")+"','"+input(" 4. ogrenci icin soyad gir \n")+"')"
    cevaplar["3"]=input(" 4. ogrenci icin cevap gir \n")
    sozluk["4"]="('"+input(" 5. ogrenci icin ad gir \n")+"','"+input(" 5. ogrenci icin soyad gir \n")+"')"
    cevaplar["4"]=input(" 5. ogrenci icin cevap gir \n")
    #print(sozluk)
    #print(cevaplar)
    puan=0
    toplam=0
    for k in range(0,5):
        for i in range(0,len(anahtar)):
            if anahtar[i]==cevaplar[str(k)][i]:
                puan=puan+10
            puanlar[str(k)]=puan
        toplam=puan+toplam
        puan=0
    
    ortalama=toplam/5
    ortalamalar={}
    sonsozluk={}
    for h in range(0,5):
        if ortalama<int(puanlar[str(h)]):
            ortalamalar[sozluk[str(h)]]=str(puanlar[str(h)])
        sonsozluk[str(sozluk[str(h)])]=str(puanlar[str(h)])
    print("\n sinif not listesi= ")
    print(sonsozluk)
    print("ortalama= "+str(ortalama))
    print("ortalamayi gecenler \n")
    
    print(ortalamalar)
    aaa=input("cikmak icin entera bas")