from re import S
import string 
#Ülesanne 1
vokaali=["a","e","u","o","i","ü","ö","ä"]
konsonanti="qwrtpsdfghklzxcvbnm"
markid=string.punctuation 
v=k=m=t=0
while True:
    tekst=input("Sissesta mingi tekst: ").lower()
    if tekst.isdigit():
        break
    else:
        tekst_list=list(tekst)
        print(tekst_list)
        for taht in tekst_list:
            if taht in vokaali:
                v+=1
            elif taht in konsonanti:
                k+=1
            elif taht in markid:
                m+=1
            elif taht == " ":
                t+=1
    print("vokaali: ",v)
    print("konsonanti: ",k)
    print("markid: ",m)
    print(" ",t)

Ülesanne 2
nimed=[]
for i in range(5):
   nimi=input(f"{i+1},:Nimi:")
   nimed.append(nimi)
print("Enne sorterimist:")
print(nimed)

nimed.sort()
print("Sorteerimise pärast:")
print(nimed)
print(f"Viimasena lisatud nimi on:{nimi}")
v=input("Kas muudame nimeid?: ").lower()
if v=="jah":
    v=input("Nimi või positsioon: N/p").upper()
    if v=="P":
        print("Sisesta nimi asukoht")
        v=int(input())
        uus_nimi=input("Uus nimi: ")
        nimed[v-1]=uus_nimi
        print(nimed)
    else:
        print("Sisesta nimi")
        vana_nimi=input("Vana nimi: ")
        v=nimed.index(vana_nimi)
        uus_nimi=input("Uus nimi: ")
        nimed[v]=uus_nimi
    print(nimed)
dublta=list(set(nimed))
print(dublta)
for nimi in nimed:
    if nimi not in dublta:
        dublta.append(nimi)
print("Mitte korduv loetlu 2.variant")
print(dublta)


#Ülesanne 2.3
vanused=[]
for i in range(7):
    vanus=int(input(f"{i+1}. Vanus: "))
    vanused.append(vanus)
print(f"Sissetatud vanused: {vanused}")
print(max(vanused))# maksimmalne arv
print(min(vanused))# minimaalne arv
print(sum(vanused)/len(vanused))# Keskmine arv

ülesanne 3
arvud=[15,18,22,24,30,14]
s=input("Sümbol: ")
for vartus in arvud:
    print(vartus*s)

#Ülesanne 4 
index_list=["Tallinn","Narva", "Narva-JõesuuKohtla-Järve", "Ida-Virumaa"," Lääne-Virumaa", "Jõgevamaa", "Tartu linn","Tartumaa", "Põlvamaa", 
       "Võrumaa","Valgamaa","Viljandimaa", "Järvamaa", "Harjumaa","Raplamaa","Pärnumaa","Läänemaa","Hiiumaa","Saaremaa"]
while 1:
    try:
        postiindex=int(input("Postiindex: "))
        if len(str(postiindex))==5:
            break
        else:
            print("On vaja 5 sümboleid!")
    except:
        print("!!!")
print("Postiindeksi analüüs: ")
index_list=list(str(postiindex))
s1=int(index_list[0])
print(f" Postiindex {postiindex} on {index_list[s1-1]}")