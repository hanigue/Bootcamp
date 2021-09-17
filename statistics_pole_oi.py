# STATISTIKA S POLEM
numbers_list = []

count_numbers = 0
count_even = 0
count_odd = 0
sum_numbers = 0


# Nacteni cisel
for i in range(0,5):
    n = int(input("Zadejte cislo: "))
    
    # Chci pouze cisla v intervalu (0,10), jinak musi zadat znova.
    # while, protoze uzivatel muze spatne cislo zadavat donekonecna
    while (n <= 0 or n >= 10): 
        n = int(input("Chyba! Zadejte cislo v intervalu! Dalsi pokus: "))  
    
    sum_numbers += n
    numbers_list.append(n)
    
print("List vypada takto:", numbers_list)

count_numbers = len(numbers_list)

for i in range(len(numbers_list)):
    if numbers_list[i] % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

numbers_list.sort()
        
print("pocet cisel:", count_numbers)
print("pocet sudych: ", count_even)
print("pocet lichych: ", count_odd)
print("Procento lichych je: ", count_odd*100/count_numbers," %")
print("Procento sudych je:", count_even*100/count_numbers, " %")
print("Prumer je:", sum_numbers/count_numbers)
print("Max: ", numbers_list[-1])
print("Min: ", numbers_list[0])
print("Druhe nejvetsi: ", numbers_list[-2])
