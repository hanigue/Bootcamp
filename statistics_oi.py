# Statistika cisel ukol (bez listu)

numbers = ''
count_number = 0
sum_numbers = 0

count_even = 0
count_odd = 0

maxim = 0
minim = float("Inf") # takhle se dela nekonecno. U maxima lze udelat float("-Inf")
second_maxim = 0

# Nacitam vstup
for i in range(0,5):
    n = int(input("Zadejte cislo: "))

    # Chci pouze cisla v intervalu (0,10), jinak musi zadat znova.
    while n <= 0 or n >= 10: # while, protoze uzivatel muze zadavat donekonecna spatne
        n = int(input("Chyba! Zadejte cislo v intervalu! Dalsi pokus:"))    
    
    numbers += str(n) + ' '
    count_number += 1
    sum_numbers += n
    
    # Hledani maxima
    if n > maxim:
        second_maxim = maxim
        maxim = n
    elif n > second_maxim:
        second_maxim = n
    
    # Hledani minima
    if n < minim:
        minim = n
        
    # Hledani lichosti a sudosti  
    if n % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print()
print("Nactena cisla jsou:", numbers)
# Statistika cisel
print("Pocet nactenych cisel: ", count_number)
print("Pocet sudych: ", count_even)
print("Pocet lichych: ", count_odd)
print("Procento lichych", count_odd*100/count_number)
print("Procento sudych", count_even*100/count_number)
print("Prumer:", sum_numbers/count_number)
print("Maximum: ", maxim)
print("Minimum: ", minim)
print("Druhe nejvetsi: ", second_maxim)


