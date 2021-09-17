# ========== SELECTION SORT ===============
import random

# Inicializace generatoru pseudonahodnych cisel
# Sekvence bude stejna i po nekolika spustenich
# Zkuste zmenit cislo pro generovani jine sekvence
random.seed(3) 

our_list = []
#-----------------------------------
# generuji 5 nahodnych cisel a ukladam do listu
for i in range(5):
    our_list.append(random.randint(1, 10))
print("List before sorting:", our_list)
# ----------------------------------

# Selection sort implementation begin =======
""" Selection sort najde minimum a da ho dopredu. Ulohu si rozlozime na nekolik podcasti:
    1. Najdi minimum
    2. Dej minimum dopredu
    3. Opakuj na neserazene casti listu.
    
    Abychom vedeli, kde je neserazena cast listu, potrebujeme si ukladat aktualni index nejmensiho cisla (promenna index).
    V tomto pripade seradime prvky sestupne. Pro vzestupne serazeni najdeme misto minima, maximum.
     """

list_length = len(our_list)
smallest_element = our_list[0] # zacni na prvnim elementu v listu
index = 0 # index nejmensiho elementu

# Prochazime od 0 do delky listu
for elem in range(list_length):
    smallest_element = our_list[elem] # potrebujeme se vratit pouze k casti, ktera je neserazena
    index = elem # prenastaveni indexu nejmensiho cisla
    
    # Nachazeni minima
    # Jdeme od elem do delky listu, jelikoz potrebujeme jit jen od neserazene casti do konce
    for i in range(elem, list_length):
        # pokud najdeme mensi cislo, tak ho prenastavime        
        if our_list[i] < smallest_element:
            smallest_element = our_list[i]
            index = i # prenastavujeme index nejmensiho cisla
    
    
    our_list.pop(index) # odstranim z naseho listu nejmensi prvek
    our_list.insert(0,smallest_element) # dam ho na zacatek pole

    # pote, co najdeme nove minimum a dame ho na na zacatek pole, spusti se novy beh vnejsiho for cyklu (posuneme se dale v listu)
    # nove minimum nachazime pouze v neserazene oblasti, protoze ve vnitrnim cyklu jdeme od elem do delky listu a ne od zacatku
    
print("List after sorting:", our_list)
