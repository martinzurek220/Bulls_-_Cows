"""
bulls_and_cows.py: druhý projekt do Engeto Online Python Akademie
author: Martin Žůrek
email: zurek.m@email.cz
discord: MartinZ#0894
"""

import os
import datetime
import time

# TODO dodelat, ze pokud txt soubor neexistuje, tak at se vygeneruje
# TODO Ve videu Engeta od Petra
# TODO odehrany csa bez milisekund

popis_hry_a_pravidla = """------------------------------------------------------
Vygeneroval jsem pro tebe 4 tajne nahodne cislice
(napr.: 1578) a tvym ukolem je uhodnout je.
Pro zadani cisla pouzij klavesnici.
------------------------------------------------------
Upresneni:          
Hra po zadani cisla vypise pocet bulls a cows
1 bull = pokud uzivatel uhodne jak cislo, tak jeho umisteni
1 cow = pokud uzivatel uhodne jak cislo, ale ne jeho umisteni

Priklad:
Tajne cislo:  1257
Zadane cislo: 1520
Vysledek: 1 bulls / 2 cow
------------------------------------------------------
Pravidla:
Cislo musi mit 4 znaky.
Cislo nesmi zacinat nulou.
V cisle nesmi byt duplicity (cisla se nesmi opakovat)
------------------------------------------------------    
Pojdme hrat.
------------------------------------------------------"""


# TODO dodelat docstring
def volba_hlavniho_menu(nazev_hry: str) -> str:
    """


    :param nazev_hry:
    :return:
    """
    print(
        "Ahoj hraci!\n"
        f"Vitam te ve hre {nazev_hry}\n"
        "V hlavnim menu zvol na klavesnici jednu z moznosti.\n"
        "------------------------------------------------------\n"
        "Hlavni menu:\n"
        " 1 - Nova hra\n"
        " 2 - Popis hry a pravidla\n"
        " 3 - Statistiky\n"
        " q - Konec hry\n"
        "------------------------------------------------------"
     )
    volba_menu = input("Zvol menu (1/2/3/q): ")
    return volba_menu


# TODO Jaky je navratovy typ?
# TODO dodelat docstring
def overeni_spravnosti_uzivatelem_zadaneho_cisla(zadane_cislo: str) -> bool:
    """


    :param zadane_cislo:
    :return:
    """
    parametry_cisla_ok = False

    # Zjisteni, jestli ma uzivatelem zadane cislo povolene parametry
    if zadane_cislo.isdecimal():
        # Pocet cislic v cisle je od 1 do 3.
        if (len(zadane_cislo)) >= 1 and len(zadane_cislo) <= 3:
            print(
                "Pocet zadanych cislic je mensi nez 4\n"
                "------------------------------------------------------"
            )
        # Pocet cislic v cisle = 4.
        elif len(zadane_cislo) == 4:
            # Je prvni cislice v cisle nula?
            if zadane_cislo[0] == "0":
                print(
                    "Cislo nesmi zacinat nulou\n"
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
                            "V zadanem cisle jsou duplicity\n"
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
                "Pocet zadanych cislic je vetsi nez 4\n"
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


def spocitej_odehrany_cas(pocatecni_cas: datetime, konecny_cas: datetime) -> list:
    """


    :param pocatecni_cas: datetime
    :param konecny_cas: datetime
    :return: [hodiny, minuty, sekundy]
    """
    odehrany_cas = konecny_cas - pocatecni_cas
    odehrany_cas.total_seconds()
    hodiny, reminder = divmod(odehrany_cas.total_seconds(), 3600)
    hodiny = hodiny % 24
    minuty, sekundy = divmod(reminder, 60)
    return [int(hodiny), int(minuty), int(sekundy)]


# TODO dodelat docstring
def urci_koncovku(pocet: int, koren_slova: "str") -> str:
    """


    :param pocet:
    :param koren_slova:
    :return:
    """
    if pocet == 0 or pocet == 1:
        slovo_s_koncovkou = koren_slova
    else:
        slovo_s_koncovkou = koren_slova + "s"
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
    file = open(nazev_txt_souboru, "a")
    file.write("\n" + str(obsah))
    file.close()


def main():

    nazev_souboru = "Statistiky_hry.txt"

    while 1:
        # Zapis do souboru zakazan
        zapis_povolen = False
        os.system("cls")
        zvolene_menu = volba_hlavniho_menu("bulls and cows")
        hra_dokoncena = ""

        # 1 - Nova hra
        if zvolene_menu == "1":

            # Iniciace promennychs
            pocet_bulls = 0
            pocet_cows = 0
            pocet_pokusu = 0
            os.system("cls")

            print("------------------------------------------------------")
            print("Pro predcasne ukonceni hry zmackni klavesu: q")
            print("------------------------------------------------------")

            while pocet_bulls != 4:
                zadane_cislo_ok = False
                uzivatelem_zadane_cislo = input("Zadej 4ciferne cislo: ")
                # TODO dodelat rand funkci
                tajne_cislo = "1234"
                pocet_pokusu += 1
                time_start_hry = vytvor_casovou_znacku()

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
                        "Nezadal jsi cislo\n"
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
                            f"Spravne, uhodl jsi tajne cislo.\n",
                            f"Pocet pokusu: {pocet_pokusu}\n",
                            f"Odehrany cas:   {odehrany_cas_string},"
                            f"\n------------------------------------------------------",
                            sep=""
                        )
                        print(time_start_hry)
                        print(time_konec_hry)
                        input("Pro navrat do hlavniho menu zadej pismeno q: ")
                        hra_dokoncena = "Ano"
                        zapis_povolen = True


        # Pokud je povolen zapis do txt souboru, uloz do nej data odehrane hry
        if zapis_povolen:
            # Zpracovani dat jedne odehrane hry
            if hra_dokoncena == "Ano":
                radek = "Start hry: " + str(time_start_hry[1]) + ", Dokonceno: " \
                        + hra_dokoncena + ", Pocet pokusu: " + str(pocet_pokusu) \
                        + ", Odehrany cas: " + odehrany_cas_string
            else:
                radek = "Start hry: " + str(time_start_hry[1]) + ", Dokonceno: " \
                        + hra_dokoncena
            zapis_do_txt_souboru(nazev_souboru, radek)

        # Popis hry a pravidla
        if zvolene_menu == "2":
            os.system("cls")
            print(popis_hry_a_pravidla)
            input("\nPro navrat do hlavniho menu stiskni ENTER: ")

        # Zobrazeni statistik
        if zvolene_menu == "3":
            os.system("cls")
            print(nacti_txt_soubor(nazev_souboru))
            input("\nPro navrat do hlavniho menu stiskni ENTER: ")

        # Konec programu
        if zvolene_menu == "q":
            break


if __name__ == "__main__":
    main()
