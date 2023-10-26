import os

class Opis_Programu:

    def zwroc(cls):
        return """ 

Witaj w programie Giton. Jest to narzędzie, które pomaga w pracy 
z programem Git. Zaczynamy.

"""

class Polecenie:

    def wykonaj(cls, polecenie):
        os.system(polecenie)

def wykonaj(komenda):
    polecenie = Polecenie()
    polecenie.wykonaj(komenda)

class Komendy_ustawien_git:

    def __init__(self):
        self.ustawienia = """git config --global"""
    
    def ustawienia(self):
        return self.ustawienia

    def uzytkownik(cls):
        return """user.name"""

    def email(cls):
        return """user.email"""

    def edytor(cls):
        return """code.editor"""

class Komendy_wyswietlania_git:

    def __init__(self):
        self.ustawienia = Komendy_ustawien_git()

    def ustawienia(self):
        return self.ustawienia

    def uzytkownik(self):
        return """git config --global user.name"""

class Komendy_konfiguracji_git:

    def __init__(self):
        self.konfiguruj = """git config --global """

    def uzytkownik(self, nazwa):
        return self.konfiguruj + """user.name '""" + nazwa + """' """

    def email(self, nazwa):
        return self.konfiguruj + """user.email """ + nazwa

    def edytor(self, nazwa):
        return self.konfiguruj + """code.editor """ + nazwa

class Komendy_git:

    def __init__(self):
        self.komenda = Komendy_konfiguracji_git()
        self.komendy_wyswietlania = Komendy_wyswietlania_git()

    def inicjuj(cls):
        return """git init"""

    def dodaj(cls):
        return """git add . """

    def opisz(cls, opis):
        return """git commit -m """ + opis

    def dodaj_i_opisz(cls, opis):
        return """git commit -a -m """ + opis

    def podlacz(cls, link):
        return """git remote add origin """ + link

    def wczytaj(cls):
        return """git push -u origin master"""

    def klonuj(csl, link):
        return """git clone """ + link

    def konfiguracja(cls):
        konfiguracja = Komendy_konfiguracji_git()
        return konfiguracja

    def uzytkownik(self, nazwa):
        return self.komenda.uzytkownik(nazwa)

    def email(self, adres):
        return self.komenda.email(adres)

    def edytor(self, nazwa):
        return self.komenda.edytor(nazwa)

    def pokaz_uzytkownika(self):
        return self.komendy_wyswietlania.uzytkownik()

class Git:

    def __init__(self):
        self.komenda = Komendy_git()

    def inicjuj(self):
        wykonaj(self.komenda.inicjuj())

    def dodaj(self):
        wykonaj(self.komenda.dodaj())

    def opisz(self, opis):
        wykonaj(self.komenda.opisz(opis))

    def dodaj_i_opisz(self, opis):
        wykonaj(self.komenda.dodaj_i_opisz(opis))

    def podlacz(self, link):
        wykonaj(self.komenda.podlacz(link))

    def wczytaj(self):
        wykonaj(self.komenda.wczytaj())

    def uzytkownik(self, nazwa):
        wykonaj(self.komenda.uzytkownik(nazwa))

    def email(self, adres):
        wykonaj(self.komenda.email(adres))

    def edytor(self, nazwa):
        wykonaj(self.komenda.edytor(nazwa))

    def pokaz_uzytkownika(self):
        wykonaj(self.komenda.pokaz_uzytkownika())

    def klonuj(self, link):
        wykonaj(self.komenda.klonuj(link))


class Stworz_program:

    def git(cls):
        return Git()

stworz_program = Stworz_program()

git = stworz_program.git()

class Inicjacja:

    def inicjuj(cls):
        git.inicjuj()
        git.dodaj_i_opisz('Inicjacja repozytorium')
        link = input("Podaj link do repozytorium: ")
        git.podlacz(link)
        git.wczytaj()

opis_programu = Opis_Programu()

opis = opis_programu.zwroc()

print(opis)

class Ekran_glowny:
    def wyswietl(self):
        opis_opcji = """
1. Konfiguracja.
2. Dzialanie.
3. Ustawienia.
4. O programie.
5. Wyjście."""
        print(opis_opcji)

    def wybierz(self):
        ekrany = (Ekran_konfiguracji(), Ekran_dzialania(), Ekran_ustawien())
        numer_opcji = int("1")
        while(numer_opcji >= 0):
            self.wyswietl()
            opcja = input("Opcja: ")
            numer_opcji = int(opcja)

            if numer_opcji == 1:
                ekran_konfiguracji = ekrany[0]
                ekran_konfiguracji.wyswietl()
            
            if numer_opcji == 2:
                ekran_dzialania = ekrany[1]
                ekran_dzialania.wyswietl()

            if numer_opcji == 3:
                ekran = ekrany[2]
                ekran.wyswietl()

            if numer_opcji == 5:
                numer_opcji = -1

class Ekran_konfiguracji:

    def __init__(self):
        self.opis_opcji = """
Wybierz jedną z opcji:
1. Użytkownik.
2. E-mail.
3. Edytor.
4. Powrót."""

    def wyswietl(self):
        opcja = ("1")
        numer_opcji = int(opcja)
        
        while(numer_opcji >= 0):
            print(self.opis_opcji)
            opcja = input("Podaj numer opcji: ")
            numer_opcji = int(opcja)
            if numer_opcji == 1:
                nazwa = input("Podaj nazwę użytkownika: ")
                git.uzytkownik(nazwa)

            if numer_opcji == 2:
                adres_email = input("Podaj adres e-mail: ")
                git.email(adres_email)
            
            if numer_opcji == 3:
                nazwa = input("Podaj nazwę edytora: ")
                git.edytor(nazwa)

            if numer_opcji == 4:
                numer_opcji = -1

class Ekran_dzialania:

    def __init__(self):
        self.opis_opcji = """Wybierz jedną z opcji:
1. Inicjacja.
2. Dodaj.
3. Opisz.
4. Dodaj i opisz.
5. Zdalnie.
6. Wczytaj.
7. Klonuj.
8. Powrót.
""" 

    def wyswietl(self):
        numer_opcji = int("1")

        while numer_opcji >= 0:
            print(self.opis_opcji)
            opcja = input("Opcja: ")
            numer_opcji = int(opcja)
    
            if numer_opcji == 1:
                git.inicjuj()

            if numer_opcji == 2:
                git.dodaj()

            if numer_opcji == 3:
                opis = input("Opis zmian: ")
                git.opisz(opis)

            if numer_opcji == 4:
                opis = input("Opis zmian: ")
                git.dodaj_i_opisz(opis)

            if numer_opcji == 5:
                link = input("Link do repozytorium: ")
                git.podlacz(link)

            if numer_opcji == 6:
                git.wczytaj()

            if numer_opcji == 7:
                link = input("Podaj link do repozytorium: ")
                git.klonuj(link)

            if numer_opcji == 8:
                numer_opcji = -1


class Ekran_ustawien:

    def __init__(self):
        self.opis_opcji = """Wyświetl ustawienia:
1. Nazwa użytkownika.
2. Wróć."""

    def wyswietl(self):
        numer_opcji = int("0")
        
        while numer_opcji >= 0:
            print(self.opis_opcji)
            opcja = input("Podaj numer opcji: ")
            numer_opcji = int(opcja)

            if numer_opcji == 1:
                git.pokaz_uzytkownika()

            if numer_opcji == 2:
                numer_opcji = -1

ekran = Ekran_glowny()
ekran.wybierz()
