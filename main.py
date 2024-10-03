# 1. Išveskite visus skaičius nuo 1 iki 20.
# su for
# for i in range(1, 21):
#     print(i)
from turtle import TurtleGraphicsError

# su while
# skaicius = 0
# while skaicius < 21:
#     print(skaicius)
#     skaicius += 1


# 2. Išveskite visus skaičius nuo 1 iki 50. Prie kiekvieno lyginio skaičiaus
# parašykite žodį "lyginis", o prie kiekvieno nelyginio – "nelyginis".

# skaicius = 1
# while skaicius <= 50:
#     if skaicius % 2 == 0:
#         print(f"{skaicius} - lyginis")
#     else:
#         print(f"{skaicius} - nelyginis")
#     skaicius += 1



# 3. Išveskite visus skaičius nuo 25 iki 50. Vietoj skaičių, kurie dalinasi iš 3
# išveskite tekstą "dalinasi iš 3".

# skaicius = 25
# while skaicius < 50:
#     if skaicius % 3 == 0:
#         print(f" {skaicius} dalinasi is 3")
#     skaicius += 1


# 4. Išveskite visus skaičius nuo 1 iki 100 arba iki tol kol pasitaikys toks, kuris
# dalinasi iš 7.

# skaicius = 1
# while skaicius < 100:
#     if skaicius % 7 == 0:
#         print(f"{skaicius} dalinasi is 7")
#         break
#     print(skaicius)
#     skaicius += 1

# 5. Išvedinėkite visus skaičius nuo 1 iki tol kol pasitaikys skaičius, kuris
# dalinasi iš 3 ir iš 5.

# skaicius = 1
# while True:
#     if skaicius % 3 ==0 and skaicius % 5 == 0:
#         print(f"{skaicius} = dalinasi is 3 ir is 5 ")
#         break
#     print(skaicius)
#     skaicius += 1

# 6. Vartotojas turi suvesti rėžių pradžią ir pabaigą. Tačiau jūs turite patikrinti
# ar nurodyti rėžiai yra geri (pradžia mažesnė už pabaigą). Liepkite
# vartotojui kartoti įvedimą tol, kol rėžiai jau bus įvesti tinkamai. Turint
# tinkamus rėžius, išveskite visus skaičius nuo rėžių pradžios iki pabaigos
# (šitam jau vietoj while galite naudoti for ciklą), šalia kiekvieno skaičiaus
# išvedant jo kvadratą, bei ar jis lyginis/nelyginis.


# a = int(input("Iveskite reziu pradzios skaiciu\n"))
# b = int(input("Iveskite reziu pabaigos skaiciu\n"))
# while True:
#     if a < b:
#         break
#     else:
#         print("Reziai nera teisingi, bandykite dar karta, (pirmas rezis turi buti mazesnis uz antraji)")
# for i in range(a, b + 1):
#     kv = i ** 2
#     lyg = "lyginis" if i % 2 == 0 else "nelyginis"
#     print(f"{i} - kvadratas: {kv}, skaiciaus tipas: {lyg}")


# 7. Išveskite visus skaičius nuo 1 iki kol pasitaikys toks, kuris yra pirminis ir yra didesnis nei 20.

# skaicius = 1
# while True:
#     if skaicius > 20:
#         print(f"{skaicius} > 20 del to yra isvestas")
#         break
#     print(skaicius)
#     skaicius += 1

# skaicius = 1
# while True:
#     skaicius += 1
#     print(skaicius)
#     if skaicius > 20:
#         isPrime = True
#         for i in range(2, skaicius - 1):
#             if skaicius % i == 0:
#                 isPrime = False
#         if isPrime:
#             break



# 8. Liepkite vartotojui įvedinėti bet kokius skaičius. Vykdykite įvedinėjimą iki
# kol įvestas skaičius bus lygus 0. Raskite įvestų skaičių sumą.
# suma = 0
# while True:
#     skaicius = int(input("Iveskite norima skaiciu "))
#     if skaicius == 0:
#         break
#     print(f"Ivestas skaicius {skaicius} nelygus 0")
#     suma += skaicius
# print(f"Is viso ivestu skaiciu suma: {suma}")




# 9. Leiskite vartotojui atlikti norimus skaičiavimus tiek kartų kiek jis nori.
# Pavyzdžiui, leiskite vartotojui įvesti du skaičius, tuomet jam parodykite
# pačius skaičius, veiksmus (sudėtis, atimtis, daugyba, dalyba) ir
# suskaičiuotus atsakymus (5 + 3 = 8; 5 - 3 = 2; ...). Kai atsakymai bus
# parodyti, vartotojas turi turėti galimybę pakartoti skaičiavimus, todėl
# leiskite pasirinkti ar dar kartoti veiksmą, ar jau programa turėtų baigti
# savo darbą.

# while True:
#     a = int(input("Iveskite pirmaji norima skaiciu: "))
#     b = int(input("Iveskite antraji norima skaiciu: "))
#     print(f"Nr. 1 pasirinktas skaicius - {a}")
#     print(f"Nr. 2 pasirinktas skaicius - {b}")
#     sud = (a + b)
#     at = (a - b)
#     daug = (a * b)
#     dalyba = (a / b)
#     print(f"Veiksmai su siais skaiciais:\nSudetis: {a} + {b} = {sud}\nAtimtis: {a} - {b} = {at}\nDaugyba: {a} * {b} = {daug}\nDalyba: {a} / {b} = {round(dalyba, 2)}")
#     kartoti = input("Ar norite kartoti skaiciavimus ? (t/n): ")
#     if kartoti != 't':
#         print("daugiau nekartojama")
#         break
# print("The End")


# 10.Vartotojui išveskite pasirinkto skaičiaus daugybos lentelę (pvz, skaičiaus 5
# daugybos lentelė būtų 5 * 1 = 5; 5 * 2 = 10; 5 * 3 = 15; ...). Leiskite
# vartotojui kartoti veiksmą (tiek kartų kiek norės) ir gauti dar vieną
# daugybos lentelę su kitu pasirinktu skaičiumi.

# while True:
#     sk = int(input("Iveskite norima skaiciu - bus isvesta skaiciaus daugybos lentele "))
#     for i in range(1, 11):
#         print(f"{sk} * {i} = {sk * i}")
#     kartoti = input("Ar norite kartoti - (t/n)? ")
#     if kartoti != 't':
#         print("Nebekartojame")
#         break

# 11.Liepkite vartotojui įvesti kiek jis nori skaičių. Įvedimą sustabdykite tuomet,
# kai vartototojas įves 0 ar -1, ar kitą jūsų pasirinktą skaičių ar simbolį.
# Raskite vartotojo įvestų skaičių sumą, vidurkį.
# skaiciai = []
# while True:
#     ivedimas = int(input("Iveskite skaiciu: (0 ar -1 stabdys programa) "))
#     if ivedimas == 0 or ivedimas == -1:
#         break
#     skaiciai.append(ivedimas)
#     kartoti = input("Ar norite kartoti - (t/n) ")
#     if kartoti != 't':
#         print(skaiciai)
#         print(f"suma: {sum(skaiciai)}, vidurkis: {sum(skaiciai) / len(skaiciai)}")


# 12.Sukurkite studentų pažymių vidurkių skaičiuoklę (kaip pavyzdį galite
# naudoti 17-ą pavyzdį). Tačiau tokia skaičiuoklė turėtų leisti skaičiuoti
# vidurkį ne tik iš vieno studento pažymių, bet leistų pakartoti pažymių
# įvedimą ir vidurkio skaičiavimą ant tiek studentų kiek reikia.




# 13.Sukurkite skaičiaus atspėjimo užduotį. Leiskite vartotojui pasirinkti
# žaidimo sudėtingumą (atsitiktinio skaičiaus rėžiai), ar suteikiamos
# pagalbos (skaičius mažesnis/didesnis nei spėjamas), kiek spėjimų
# leidžiama (neribotai, arba pvz iki 10 ėjimų), bei kiti pasirinkti parametrai.
# Vartotojas šiuos parametrus pasirenka žaidimo pradžioje. Turite užtikrinti,
# kad vartotojas pasirinko parametrus tik iš galimų - jeigu ne, liepkite
# įvedimą pakartoti.