"""
bulls_and_cows.py: druhý projekt do Engeto Online Python Akademie
author: Martin Žůrek
email: zurek.m@email.cz
discord: MartinZ#0894
"""

import os
import datetime
import random

popis_hry_a_pravidla = """------------------------------------------------------
Vygeneroval jsem pro tebe 4 tajné náhodné číslice
(např.: 1578) a tvým úkolem je uhodnout je.
Pro zadání čísla použij klávesnici.
------------------------------------------------------
Upřesnění:          
Hra po zadání čísla vypíše počet bulls a cows
1 bull = pokud uživatel uhodne jak číslo, tak jeho umístění
1 cow = pokud uživatel uhodne číslo, ale ne jeho umístění

Příklad:
Tajné číslo:  1257
Zadané číslo: 1520
Výsledek: 1 bulls / 2 cow
------------------------------------------------------
Pravidla:
Číslo musí mít 4 znaky.
Číslo nesmí začínat nulou.
V čísle nesmí být duplicity (čísla se nesmí opakovat)
------------------------------------------------------"""


def volba_hlavniho_menu(nazev_hry: str) -> str:
    """
    Funkce vygeneruje hlavní menu.

    :param nazev_hry: "nazev_hry"
    :return: "volba_menu"
    """
    print(
        "Ahoj hráči!\n"
        f"Vítám tě ve hře {nazev_hry}.\n"
        "V hlavním menu zvol na klávesnici jednu z možností.\n"
        "------------------------------------------------------\n"
        "Hlavní menu:\n"
        " 1 - Nová hra\n"
        " 2 - Popis hry a pravidla\n"
        " 3 - Statistiky\n"
        " q - Konec hry\n"
        "------------------------------------------------------"
     )
    volba_menu = input("Zvol menu (1/2/3/q): ")
    return volba_menu


def vygeneruj_tajne_cislo() -> str:
    """
    Funkce vygeneruje cislo od 1000 do 9999.
    V cisle nebudou duplicity.

    Příklad výsledku:

    "1258"

    :return: "vygenerovane_tajne_cislo"
    """
    vygenerovane_tajne_cislo = 0
    vygenerovane_tajne_cislo_ok = False

    while not vygenerovane_tajne_cislo_ok:
        r = random.randrange(1000, 10000, 1)
        vygenerovane_tajne_cislo = str(r)
        soucet = 0

        for cislo in vygenerovane_tajne_cislo:
            soucet += vygenerovane_tajne_cislo.count(cislo)
        if soucet > 4:
            vygenerovane_tajne_cislo_ok = False
        else:
            vygenerovane_tajne_cislo_ok = True

    return vygenerovane_tajne_cislo


def overeni_spravnosti_uzivatelem_zadaneho_cisla(zadane_cislo: str) -> bool:
    """
    Funkce overi uzivatelem zadane cislo.

    :param zadane_cislo: "zadane_cislo"
    :return: cislo_ok_nok
    """
    parametry_cisla_ok = False

    # Zjisteni, jestli ma uzivatelem zadane cislo povolene parametry
    if zadane_cislo.isdecimal():
        # Pocet cislic v cisle je od 1 do 3.
        if (len(zadane_cislo)) >= 1 and len(zadane_cislo) <= 3:
            print(
                "Počet zadaných číslic je menší než 4\n"
                "------------------------------------------------------"
            )
        # Pocet cislic v cisle = 4.
        elif len(zadane_cislo) == 4:
            # Je prvni cislice v cisle nula?
            if zadane_cislo[0] == "0":
                print(
                    "Číslo nesmí začínat nulou\n"
                    "------------------------------------------------------"
                )
            # Pokud neni prvni cislice v cisle nula.
            else:
                # Cyklus vezme jednotlive cisla v uzivetelem zadanem cisle
                # a pomoci funkce count spocita pocet vyskytu.
                for pocet_stejnych_cisel in set(zadane_cislo):
                    # Pokud je pocet vyskytu dva a vice
                    if zadane_cislo.count(pocet_stejnych_cisel) > 1:
                        print(
                            "V zadaném čísle jsou duplicity\n"
                            "------------------------------------------------------"
                        )
                        break
                # Pokud se kazda cislice v cisle vyskytuje pouze jednou.
                else:
                    parametry_cisla_ok = True
                    # print("Zadane cislo ma spravny format")
        # Pocet cislic v cisle je 5 a vice.
        elif len(zadane_cislo) >= 5:
            print(
                "Počet zadaných číslic je větší než 4\n"
                "------------------------------------------------------"
            )
    return parametry_cisla_ok


def vytvor_casovou_znacku() -> list:
    """
    Funkce vytvori casovou znacku.

    Priklad vystupu:

    [2022-10-07 15:10:46.387781, 07.10.2022 15:10:46]

    casova_znacka: da se scitat/odcitat s jinou casouvou znackou

    casova_znacka_tisk: pouze pro tisk treba do txt souboru

    :return: [casova_znacka, casova_znacka_tisk]
    """
    casova_znacka = datetime.datetime.now()
    casova_znacka_tisk = casova_znacka.strftime("%d.%m.%Y %H:%M:%S")
    return [casova_znacka, casova_znacka_tisk]


def spocitej_odehrany_cas(pocatecni_cas: datetime.datetime, konecny_cas: datetime.datetime) -> list:
    """
    Funkce spocita rozdil dvou casovych znacek a vrati hodnoty hodiny, minuty, sekundy.

    Pozor:

    Funkce odecita pouze casy vygenerovane funkci datetime.datetime.now().

    :param pocatecni_cas: datetime.datetime
    :param konecny_cas: datetime.datetime
    :return: [hodiny, minuty, sekundy]
    """
    odehrany_cas = konecny_cas - pocatecni_cas
    odehrany_cas.total_seconds()
    hodiny, reminder = divmod(odehrany_cas.total_seconds(), 3600)
    hodiny = hodiny % 24
    minuty, sekundy = divmod(reminder, 60)
    return [int(hodiny), int(minuty), int(sekundy)]


def urci_koncovku(pocet: int, anglicke_slovo: "str") -> str:
    """
    Funkce doplni/nedoplni koncovku 's' pro anglicke slovo.

    Priklad vystupu:

    0, 1 = bull
    2 a vice = bulls

    :param pocet:
    :param anglicke_slovo:
    :return:
    """
    if pocet == 0 or pocet == 1:
        slovo_s_koncovkou = anglicke_slovo
    else:
        slovo_s_koncovkou = anglicke_slovo + "s"
    return slovo_s_koncovkou


def nacti_txt_soubor(nazev_txt_souboru: str) -> str:
    """
    Funkce nacte po jednotlivych radcich txt soubor.

    Priklad vysledku:

    '''
    Start hry: 07.10.2022 16:00:37 Dokonceno: Ano Pokusu: 3 Cas: 0:00:03.423810
    Start hry: 07.10.2022 16:00:37 Dokonceno: Ano Pokusu: 4 Cas: 0:00:14.822241
    Start hry: 07.10.2022 16:05:46 Dokonceno: Ne
    '''

    :param nazev_txt_souboru: "nazev_txt_souboru"
    :return: ''' string '''
    """
    soubor_file = open(nazev_txt_souboru, "r")
    nacteny_soubor = soubor_file.read()
    soubor_file.close()
    return nacteny_soubor


def zapis_do_txt_souboru(nazev_txt_souboru: str, obsah: str) -> None:
    """
    Funkce zapise do txt souboru.

    :param nazev_txt_souboru: "nazev_txt_souboru"
    :param obsah: ''' string '''
    :return:
    """
    file = open(nazev_txt_souboru, "a")
    file.write("\n" + str(obsah))
    file.close()


def main():

    nazev_souboru = "Statistiky_hry.txt"

    while 1:
        # Zapis do souboru zakazan
        zapis_povolen = False
        os.system("cls")
        zvolene_menu = volba_hlavniho_menu("Bulls and cows")
        hra_dokoncena = ""

        # 1 - Nova hra
        if zvolene_menu == "1":

            # Iniciace promennychs
            pocet_bulls = 0
            pocet_cows = 0
            pocet_pokusu = 0
            start_hry = True
            os.system("cls")

            tajne_cislo = "1395"
            # tajne_cislo = vygeneruj_tajne_cislo()

            print(
                "------------------------------------------------------\n"
                "Pro předčasné ukončení hry zmáčkni klávesu: q\n"
                "------------------------------------------------------\n"
                "Pojďme hrát.\n"
                "------------------------------------------------------"
            )

            while pocet_bulls != 4:
                zadane_cislo_ok = False
                uzivatelem_zadane_cislo = input("Zadej 4ciferné číslo: ")
                pocet_pokusu += 1

                # Podm. bool_start_hry == True, aby se start spustil pouze jednou
                # na zacatku hry a nespoustel se po kazdem pokusu uzivatele.
                if start_hry:
                    time_start_hry = vytvor_casovou_znacku()
                    start_hry = False

                # Kontrola zadaneho vstupu
                if uzivatelem_zadane_cislo.isdecimal():
                    zadane_cislo_ok = overeni_spravnosti_uzivatelem_zadaneho_cisla(uzivatelem_zadane_cislo)
                # Uzivatel nic nezadal.
                elif uzivatelem_zadane_cislo == "":
                    print(
                        "Nezadal jsi nic\n"
                        "------------------------------------------------------"
                    )
                # Navrat do hlavniho menu
                elif uzivatelem_zadane_cislo == "q":
                    hra_dokoncena = "Ne"
                    zapis_povolen = True
                    break
                # Uzivatel nezadal cislo.
                else:
                    print(
                        "Nezadal jsi číslo\n"
                        "------------------------------------------------------"
                    )

                if zadane_cislo_ok:
                    # Pocet bulls a cows se po kazdem pruchodu smyckou musi smazat. Pokud se
                    # nesmaze, tak dochazi k tomu, ze se pocty inkrementuji s pocty
                    # z predchoziho kola.
                    pocet_bulls = 0
                    pocet_cows = 0

                    # Spocita pocet bulls
                    for idx_bull, cislo_bull in enumerate(uzivatelem_zadane_cislo):
                        if cislo_bull == tajne_cislo[idx_bull]:
                            pocet_bulls += 1

                    # Spocita pocet cows
                    for idx, cislo_cow in enumerate(uzivatelem_zadane_cislo):
                        for idx_2, cislo_tajne in enumerate(tajne_cislo):
                            if cislo_cow == cislo_tajne and idx != idx_2:
                                pocet_cows += 1
                    koncovka_bull_bulls = urci_koncovku(pocet_bulls, "bull")
                    koncovka_cow_cows = urci_koncovku(pocet_cows, "cow")
                    print(
                        f"{pocet_bulls} {koncovka_bull_bulls} / "
                        f"{pocet_cows} {koncovka_cow_cows}\n"
                        f"------------------------------------------------------"
                    )

                    if pocet_bulls == 4:
                        time_konec_hry = vytvor_casovou_znacku()
                        odehrany_cas = spocitej_odehrany_cas(time_start_hry[0], time_konec_hry[0])
                        odehrany_cas_string = f"{odehrany_cas[0]} hod : {odehrany_cas[1]} min : " +\
                                              f"{odehrany_cas[2]} sek"
                        print(
                            f"Správně, uhodl jsi tajné číslo.\n",
                            f"Počet pokusů: {pocet_pokusu}\n",
                            f"Odehraný čas:   {odehrany_cas_string}",
                            f"\n------------------------------------------------------",
                            sep=""
                        )
                        input("Pro návrat do hlavního menu zadej písmeno q: ")
                        hra_dokoncena = "Ano"
                        zapis_povolen = True

        # Pokud je povolen zapis do txt souboru, uloz do nej data odehrane hry
        if zapis_povolen:
            # Zpracovani dat jedne odehrane hry
            if hra_dokoncena == "Ano":
                radek = "Start hry: " + str(time_start_hry[1]) + ", Dokončeno: " \
                        + hra_dokoncena + ", Počet pokusů: " + str(pocet_pokusu) \
                        + ", Odehraný čas: " + odehrany_cas_string
            else:
                radek = "Start hry: " + str(time_start_hry[1]) + ", Dokončeno: " \
                        + hra_dokoncena
            zapis_do_txt_souboru(nazev_souboru, radek)

        # Popis hry a pravidla
        if zvolene_menu == "2":
            os.system("cls")
            print(popis_hry_a_pravidla)
            input("\nPro návrat do hlavního menu stiskni ENTER: ")

        # Zobrazeni statistik
        if zvolene_menu == "3":
            os.system("cls")

            # True/False podle toho, jestli txt soubor ve slozce je nebo ne
            overeni_existence_txt_souboru = os.path.isfile(nazev_souboru)

            if overeni_existence_txt_souboru:
                print(nacti_txt_soubor(nazev_souboru))
            else:
                print("K dispozici zatím nejsou žádné statistiky odehraných her")

            input("\nPro návrat do hlavního menu stiskni ENTER: ")

        # Konec programu
        if zvolene_menu == "q":
            break


if __name__ == "__main__":
    main()
