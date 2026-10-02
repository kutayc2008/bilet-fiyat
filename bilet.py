isim = input("Adın nedir?")
yaş = input("kaç yaşındasın?")
yaş = int(yaş)

öğrenci = input("öğrenci misin? (evet/hayır)")

if yaş < 12:
        print("Senin için bilet fiyatı 50 TL")
elif yaş >= 12 and yaş < 18:
    print("Senin için bilet fiyatı 70 TL")
elif öğrenci.lower() == "evet":
    print(f"Merhaba {isim}, demek {yaş} yaşındasın ve öğrenciymişsin senin için bilet fiyatı 80 TL")

else:
    print(f"Merhaba {isim}, demek {yaş} yaşındasın ve öğrenci değilsin senin için bilet fiyatı 120 TL")