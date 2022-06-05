"""
projekt_2: druhý projekt do Engeto Online Python Akademie
Bulls_&_Cows.py
author: Martin Žůrek
email: zurek.m@email.cz
discord: MartinZ#0894
"""

# Poznamka:
#
# Cely kod jsem pro pochopitelnost a prehlednost rozdelil do nekolika celku:
#   - Overeni spravnosti uzivatelem zadaneho cisla

print("""Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------"""
)

str_zadane_cislo = input("Enter a number:")

print("-----------------------------------------------")


###############################################################################
# Overeni spravnosti uzivatelem zadaneho cisla                                #
###############################################################################

bool_parametry_cisla_ok = False

# Zjisteni, jestli ma uzivatelem zadane cislo povolene parametry
if str_zadane_cislo.isdecimal() == True:
    # Pocet cislic v cisle je od 1 do 3.
    if len(str_zadane_cislo) >= 1 and len(str_zadane_cislo) <= 3:
        print("Pocet zadanych cislic je mensi nez 4")
    # Pocet cislic v cisle = 4.
    elif len(str_zadane_cislo) == 4:
        # Je prvni cislice v cisle nula?
        if str_zadane_cislo[0] == "0":
            print("Cislo nesmi zacinat nulou")
        # Pokud neni prvni cislice v cisle nula.
        else:
            # Cyklus vezme jednotlive cisla v uzivetelem zadanem cisle 
            # a pomoci funkce count spocita pocet vyskytu.
            for xx_pocet_stejnych_cisel in set(str_zadane_cislo):
                # Pokud je pocet vyskytu dva a vice
                if str_zadane_cislo.count(xx_pocet_stejnych_cisel) > 1:
                    print("V zadanem cisle jsou duplicity")
                    break
            # Pokud se kazda cislice v cisle vyskytuje pouze jednou.
            else:
                bool_parametry_cisla_ok = True
                print("Zadane cislo ma spravny format")
    # Pocet cislic v cisle je 5 a vice.
    elif len(str_zadane_cislo) >= 5:
        print("Pocet zadanych cislic je vetsi nez 4")
# Uzivatel nic nezadal.
elif str_zadane_cislo == "":
    print("Nezadal jsi nic")
# Uzivatel nezadal cislo.
else:
    print("Nezadal jsi cislo")