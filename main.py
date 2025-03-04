import random
from itertools import count

# print("hi")
# number = [6,8,13,16,20]  # masyvas
# print(number)
#
# empty_list = []
# print(empty_list)
#
# empty_list.append(3) # leidzia ideti papildomai dar viena reiksme
# print(empty_list)
# empty_list.extend([12,28,30]) # prideda daugiau reiksmiu. Jie rasosi []
# print(empty_list)
#
# print(empty_list.count(28)) #suranda kiek yra ieskomos reiksmes vienetu
#
# empty_list.remove(12) # panaikina nuorodyta skaiciu
# print(empty_list)
#
# # empty_list.pop(30)
# # print(empty_list)  # panaikina paskutini elementa
#
# popped_element = empty_list.pop()
# print(popped_element)
#
# studentai = ['Naglis','Paulius','Julija','Dalia']
# print(studentai)
# studentai.sort() # dirba su orginaliu sarasu ir suriusiavus originalus sarasas pasikeicia
# print(studentai)
# studentai.sort(reverse=True) # surusiavo atvirsksciai
# print(studentai)
# #            0  1  2  3  4  5 INDEKSAI
# my_number = [1, 2, 3, 4, 5, 6]
# print(my_number) # atspausdina visas reiksmes
# print(my_number[4]) # atspausdins 5
# print(my_number[0:3]) # ima nuo 0 iki 3 neims 3 (ziureti indeksus)
# print(my_number[2:5]) # ima nuo 2 iki 5, 5 neims (ziureti indeksus)
# print((my_number[4:])) # paims skaicius nuo 4 iki tiek kiek toliau bus skaiciu
# print(my_number[:4]) #paims vius skaicius nuo pradzios iki nurodytos pozicijos, neima 4
# print(my_number[-2]) # antra pozicija nuo galo
# print(my_number[-4:]) # nuo 4 pozicijos nuo galo iki pat galo
# print(my_number[:-5]) # nuo pradzios iki 5 pozicijos nuo galo
# print(my_number[2:-1]) # nuo 2 poazijos iki 1-os nuo galo
# print(my_number[-4:-2]) # ima nuo 4 nuo galo iki 2 nuo galo
# print(my_number[:]) # paima viska nuo pradzios iki galo, kaip ir neirasius nieko
# # print(my_number[pradzia:galas:zingsnis])
# print(my_number[::2]) # paims kas antra indeksa visas indeksus
# print(my_number[1::2])# ima nuo pirmo indekso iki galo ir kas antra indeksa
# print(my_number[2:5:2]) # nuo 2 indekso iki 5 (5 neima) kas antra zingsni (indeksa)
# print(my_number[2:-2:2]) # paima viskas be pirmu 2-u ir 2-u paskutiniu kas antra
# print(my_number[::-2]) # ima viska, kas antra indeksa bet nuo galo
# print(my_number)
#
# print(len(studentai)) # suskaiciavo kiek yra studentu
# for studento_vardas in studentai: # vyksta ciklas sarase "studentai"
#     print("Studento vardas yra:")
#     print(studento_vardas)
#
# print(range(0,10)) #sukuriamas intervalas
# for number in range(0,10):
#     print(number)
#
# for i in range(0,len(studentai)): # i yra i
#     print(f'{i} - a iteracijai. bandau paimti studentai [{i}] studentas kuris yra {studentai [i]}')
#
# import random
#
# print("hi")
#
# number = 17
# numbers = [6,10,12,14,5,8]
# print(number)
# print(numbers)
#
# empty_list = []
# print(empty_list)
#
# empty_list.append(20)
# print(empty_list)
# empty_list.extend([14,20,4]) #extend naudojame lauztinius skliaustus [] ir juose isvardinam reiksmes kurias norime
# # prideti
# print(empty_list)
#
# print(empty_list.count(20)) # suranda KIEK yra ieskomos reiksmes vienetu
# empty_list.remove(14) #panaikina pirma reiskme kuri yra ieskoma reiksme
# print(empty_list)
# popped_element = empty_list.pop()
# print(empty_list)
# print(popped_element)
#
#
# students = ['Ingrida','Anzelika','Arnas','Mangirdas','Paulius','Julija','Neringa','Raimundas','Rolandas','Dalia',
#             'Edvinas','Vytautas']
# print(students)
# students.sort()
# # students.sort(reverse=True)
# print(students)
#
# #             0  1  2  3  4  5  6  7  8  9 INDEKSAI
# my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# ###################### PIRMAS PARAMETRAS INCLUSIVE, JI IMA, ANTRAS EXCLUSIVE, JO NEIMA, IMI IKI JO######################
# # print(my_numbers[pradzia:galas:zingsnis])
# print(my_numbers)#atspausdiname viska
# print(my_numbers[6])#vienas
# print(my_numbers[0:4])#nuo iki
# print(my_numbers[4:8])
# print(my_numbers[7:])#nuo iki galo
# print(my_numbers[:4])#nuo pradzios iki nurodytos pozicijos (exclusive, jos neima. IKI jos)
# print(my_numbers[-2])#antra pozicija nuo galo
# print(my_numbers[-5:])#nuo 5 pozicijos nuo galo iki pat galo
# print(my_numbers[:-5])#nuo pradzios iki 5 pozicijos nuo galo
# print(my_numbers[2:-5])# nuo 2 pozicijos iki 5tos nuo galo
# print(my_numbers[-6:-2])#imame nuo 6 nuo galo iki 2 nuo galo
# print(my_numbers[-8:4])#teoriskai veikia, neapsikraukis =D
# print(my_numbers[:])#paima viska nuo pradzios iki galo, lygiai taip pat, kaip ir neirasius nieko
# print(my_numbers[::2])#visa imtis, kas antras elementas
# print(my_numbers[::3])#visa imtis, kas 3cias elementas
# print(my_numbers[1::2])#visa imtis nuo 1o indekso iki galo, kas antras elementas
# print(my_numbers[3:7:2])#nuo 3 indekso inclusive iki 7 exclusive kas antras elementas
# print(my_numbers[2:-2:2])#paimu viska be pirmu dvieju IR paskutiniu dvieju kas antra
# print(my_numbers[::-1])#visi elementai, bet nuo galo.
# print(my_numbers[::-2])# visa imtis, kas antras elementas BET nuo GALO
#
# ### complicated sht ###
# # copy = my_numbers.copy()
# # copy.remove(7)
# # print(copy)
# # print(my_numbers)
# ### complicated sht ###
#
# print(len(students))
# for studento_vardas in students:#mokekit pradzioj bent tiek ir uzteks =p
#     print("studento vardas yra:")
#     print(studento_vardas)
#
# print("po ciklo")
#
# print("continue")
# for i in range(0,20):
#     if i % 3 == 0:#ar dalinasi is 3 be liekanos
#         continue
#     print(i)
#
# print("break")
# for i in range(1,20):
#     if i % 5 == 0:#ar dalinasi is 3 be liekanos
#         break
#     print(i)
#
#
# ############################ extra ##########################
# print(range(0,10))
#
# for number in range(0,10):#0,1,2,3.....
#     print(number)
#
# for i in range(0, len(students)):
#     print(f'{i}-a iteracija. bandau paimti students[{i}] studenta kuris yra {students[i]}')
#
# for i in range(0, len(students)):#tai kas tyliai vyksta po kapotu.
#     studento_vardas = students[i]
#     print(studento_vardas)
#
# for i in range(0, len(students)):
#     print(f'{i+1}. {students[i]}')
# ############################ extra ##########################
#
#
#
# # i = 1
# # while i < 6:#kol sita salyga grazina true, tol ciklas sukasi
# #   i += 1
# #   print(i)
#
#
# i = 0
# while True:
#     i += 1
#     print(i)
#     if i >= 10:
#         break
# print("=============================")
# dice = 0
# while dice < 6:
#     dice = random.randint(1,6)
#     print(dice)
#
# print("=============================")
# dice = 0
# while True:
#     dice = random.randint(1,6)
#     print(dice)
#     if dice == 6:
#         break
#
#
# print(10 / 2)
# print(10 % 2)
# print(12 % 5) # 10 - 5 = 7; 7 - 5 = 2;
# print(10 % 2 == 0)
#
# for y in range(1, 11):
#     row = ""
#     for x in range(1, 11):
#         row += str(y * x) + " "
#     print(row)

# Sukurkite ciklą kuris atspausdintų 10 kartų žodį “labas”
# pasisveikinimas = 'labas'
# print((pasisveikinimas) * 10)

for i in range(10):
    print('labas')

i = 0
while i <10:
    print('labas')
    i += 1

# Sukurkite ciklą kuris atspausdintų skaičius nuo 0 iki 9.

for i in range(10):
    print(i)

# Sukurkite masyvą iš dešimties augalų pavadinimų
augalai = ['roze', 'tulpe', 'narcizas', 'ramune', 'varpelis', 'berzas', 'saulegraza', 'klevas', 'fikusas', 'dilgele']
print(augalai)

# Atspausdinkite kiekvieną 3čio uždavinio augalą atskiroje eilutėje.

for augalas in augalai[::3]:
    print(augalas)
print('=========================')
# kitas variantas
# for i in range(0, len(augalai),3):
# print(augalai[i])

 # print('=========================')
 # Atspausdinkite kas antrą skaičių nuo 10 iki 50 (porinius)

for i in range(10, 51, 2):
    print(i)
print('=================')
# Atspausdinkite kas antrą skaičių nuo 10 iki 50. (porinius) Jei skaičius dalinasi iš 10 be liekanos jo nespausdinkite. ( naudokite continue.) (atspausdinti visus porinus skaičius, išskyrus tuos kurie dalinasi iš 10 be liekanos)
for i in range(10, 51, 2):
   if i % 10 !=0:
    print(i)

print('=================')
# Sukurkite ciklą kuris suktųsi nuo 0 iki 20. Suskaičiuokite, kiek kartų kintamasis i turėjo porinę reikšmę;
poriniai_sk = 0
for i in range(0,21):
    if i % 2 == 0:
        poriniai_sk+= 1
print('Poriniu reiksmiu kiekis:', poriniai_sk)
print('==================')
# Suskaičiuokite kiek 3čio uždavinio masyve yra žodžių trumpesnių nei 5 simboliai, ir kiek ilgesnių nei 7 simboliai. (du skaičiavimai)
for augalas in augalai:
    raidziu_sk = len(augalas)
    if raidziu_sk < 5:
        print(augalas)
    break
print('=========')
# Atspausdinkite 3čio uždavinio kiekvieną augalą pradedant nuo paskutinio, ir baigiant pirmuoju. (atvirkščias ciklas).
for augalas in augalai[::-1]:
    print(augalas)
print('====RAUDONAS=====')
for augalas in augalai:
    raidziu_sk = len(augalas)
    if raidziu_sk > 7:
        print(augalas)
print('=================')
# Suskaičiuokite kiek 3čio uždavinio masyve yra žodžių ilgesnių nei 5 simboliai bet trumpesnių  nei 10 simboliai. (tarp 5 ir 10 simbolių ilgio)
for augalas in augalai:
    raidziu_sk = len(augalas)
    if 5 < raidziu_sk < 10:
        print(augalas)

print('=============sunkesni===============')
# Sugeneruokite 300 atsitiktinių skaičių nuo 0 iki 300, atspausdinkite juos atskirtus tarpais ir suskaičiuokite kiek tarp jų yra didesnių už 150.  Skaičiai didesni nei 275 turi būti atspausdinti skliausteliuose” [ ] “.
for i in range(300):
    a_s = random.randint(0,300)
    if a_s > 150:
        print(i + 1, end =" ")
    if a_s > 275:
        print(f"[{a_s}]", end=" ")
    else:
        print(a_s, end =' ')
print()
print('=============sunkesni===============')
# Vienoje eilutėje atspausdinkite visus skaičius nuo 1 iki 3000, kurie dalijasi iš 77 be liekanos. Skaičius atskirkite kableliais. Po paskutinio skaičiaus kablelio neturi būti.
paskutinis = []
for i in range(3001):
    a_s = random.randint(0,3000)
    if a_s % 77 == 0:
        paskutinis.append((str(a_s))) # append - prideda skaiciu i sarasa
print(", ".join(paskutinis))
        # print(a_s, end =", ".join(paskutinis))

print('=============sunkesni===============')
# Nupieškite kvadratą iš “*”, kurio kraštines sudaro 25“*”.
# * * * * * * * * * * *
# * * * * * * * * * * *
# * * * * * * * * * * *
# * * * * * * * * * * *
# * * * * * * * * * * *
# * * * * * * * * * * *
# * * * * * * * * * * *
dydis = 25
for i in range(dydis):
    print('*' * dydis)
# Nupiesti trikampi
height = 16
for i in range(1, height + 1):
    print('*' * i)

print('=============sunkesni===============')
# Prieš tai nupieštam kvadratui nupieškite istrižaines zaigzdutę pakeisdami kitu simboliu.
dydis = 25
simbolis = "*"
kitas_simbolis = "$"

for x in range(dydis):
    eilute = ""
    for y in range(dydis):
        # Tikriname pirmąją įstrižainę (x == y) ir antrąją įstrižainę (x + y == dydis - 1)
        if x == y or x + y == dydis - 1:
            eilute += kitas_simbolis
        else:
            eilute += simbolis
    print(eilute)
print('=============sunkesni===============')
# Reikia nupaišyti pilnavidurį rombą, taip pat, kaip ir pilnavidurį kvadratą (https://lt.wikipedia.org/wiki/Rombas), kurio aukštis 21 eilutė.
hheight = 21  # Rombas turi būti 21 eilučių aukščio
simbolis = "*"

# Viršutinė rombo pusė
for i in range(height // 2 + 1):
    tarpai = " " * (height // 2 - i)  # Centravimas
    zvaigzdutes = simbolis * (2 * i + 1)
    print(tarpai + zvaigzdutes)

# Apatinė rombo pusė
for i in range(height // 2 - 1, -1, -1):
    tarpai = " " * (height // 2 - i)  # Centravimas
    zvaigzdutes = simbolis * (2 * i + 1)
    print(tarpai + zvaigzdutes)
print('=============sunkesni ROMBAS===============')

for y in range(0,21):
    row = " "
    for x in range(0,21):
        if y < x:
            row += "*"
        else:
            row += " "
    print(row)


# Metam monetą. Monetos kritimo rezultatą imituojam random.randint(x,x) funkcija, kur 0 yra herbas, o 1 - skaičius. Monetos metimo rezultatus išvedame į ekraną atskiroje eilutėje: “S” jeigu iškrito skaičius ir “H” jeigu herbas. Suprogramuokite tris skirtingus scenarijus kai monetos metimą stabdome:
# Iškritus herbui;
# Tris kartus iškritus herbui;
# Tris kartus iš eilės iškritus herbui;

herbas = "H"
skaicius = "S"

# Ciklas, kuris 3 kartus meta monetą
while True:
    a_s = random.randint(0, 1)  # Generuojame 0 arba 1 (herbas arba skaičius)
    if a_s == 0:  # Jei iškrito 0, tai herbas
            print(herbas)
            break
    else:  # Jei iškrito 1, tai skaičius
        print(skaicius)
print('============Tris kartus iškritus herbui=============')
# Tris kartus iškritus herbui;
herbu_sk = 0
while herbu_sk < 3:
    a_s = random.randint(0,1)
    if a_s == 0:
        print(herbas)
        herbu_sk += 1
    else:
        print(skaicius)
print('=======# Tris kartus iš eilės iškritus herbui=========')
# Tris kartus iš eilės iškritus herbui
herbu_sk = 0
while herbu_sk < 3:
    a_s = random.randint(0,1)
    if a_s == 0:
        print(herbas)
        herbu_sk += 1
    else:
        print(skaicius)
        herbu_sk = 0
    if herbu_sk == 3:
        break
print("iskrito 3 herbai is eiles")

print('=============sunkesni===============')
# Kazys ir Petras žaidžia šaškėm. Petras surenka taškų kiekį nuo 10 iki 20, Kazys surenka taškų kiekį nuo 5 iki 25. Vienoje eilutėje išvesti žaidėjų vardus su taškų kiekiu ir “Partiją laimėjo: laimėtojo vardas”. Taškų kiekį generuokite funkcija random.randint(x,x). Žaidimą laimi tas, kas greičiau surenka 222 taškus. Partijas kartoti tol, kol kažkuris žaidėjas pirmas surenka 222 arba daugiau taškų.

zaidejas_1 = "Petras"
zaidejas_2 = "Kazys"
petro_tasku_kiekis = 0
kazio_tasku_kiekis = 0
# petro_tasku_kiekis = random.randint(10,20)
# kazio_tasku_kiekis = random.randint(5,25)
suma_tasku = 222
print(petro_tasku_kiekis, kazio_tasku_kiekis)
# if petro_tasku_kiekis > kazio_tasku_kiekis:
#     print("Partiją laimėjo: ", (zaidejas_1))
# else:
#     print("Partiją laimėjo: ", (zaidejas_2))
while petro_tasku_kiekis < suma_tasku and kazio_tasku_kiekis < suma_tasku:
    petro_zaidimas = random.randint(10, 20)
    kazio_zaidimas = random.randint(5, 25)

    petro_tasku_kiekis += petro_zaidimas
    kazio_tasku_kiekis += kazio_zaidimas

    print(petro_tasku_kiekis, kazio_tasku_kiekis)

if petro_tasku_kiekis >= suma_tasku:
    print("Partiją laimėjo: ", (zaidejas_1))

else:
    print("Partiją laimėjo: ", (zaidejas_2))

print('=============sunkesni===============')
# Sumodeliuokite vinies kalimą. Įkalimo gylį sumodeliuokite pasinaudodami random.randint(x,x) funkcija. Vinies ilgis 8.5cm (pilnai sulenda į lentą).
# a)	“Įkalkite” 5 vinis mažais smūgiais. Vienas smūgis vinį įkala 5-20 mm. Suskaičiuokite kiek reikia smūgių.
#
vinies_ilgis = 85
total_kalimu_sk = 0
for i in range(5):
    smugio_sumavimas = 0
    kalimu_sk = 0

    while smugio_sumavimas < vinies_ilgis:
        kalimas = random.randint(5,20)
        smugio_sumavimas += kalimas
        print(kalimas)
        kalimu_sk += 1
        total_kalimu_sk += 1
    # total_kalimu_sk += kalimu_sk
    print("Ikalta.", "Ikalimui reikejo: ", kalimu_sk, "smugiu.")
print(total_kalimu_sk)
print("==========b variantas=============")
# b)	“Įkalkite” 5 vinis dideliais smūgiais. Vienas smūgis vinį įkala 20-30 mm, bet yra 50% tikimybė (pasinaudokite random.randint(x,x) funkcija tikimybei sumodeliuoti), kad smūgis nepataikys į vinį. Suskaičiuokite kiek reikia smūgių.
vinies_ilgis = 85
total_kalimu_sk = 0
for i in range(5):
    smugio_sumavimas = 0
    kalimu_sk = 0

    while smugio_sumavimas < vinies_ilgis:
        if random.randint(0,1) == 1:
            kalimas = random.randint(20,30)
            smugio_sumavimas += kalimas
            print(kalimas)
            kalimu_sk += 1
            total_kalimu_sk += 1
    # total_kalimu_sk += kalimu_sk
    print("Ikalta.", "Ikalimui reikejo: ", kalimu_sk, "smugiu.")
print(f"Visu viniu ikalimui reikejo {total_kalimu_sk} smugiu")


# git config --global user.email "luckyjulija@yahoo.com"
# git config --global user.name "julijaskr"
print("Pasijungiau")

print("2025-03-04")






