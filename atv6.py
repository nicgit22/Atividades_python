numero = int(input("numero: "))

if numero <= 1:
    print("esse numero não é primo")
else:
    e_primo = True 
    
   
    for i in range(2, numero):
        if numero % i == 0:
            e_primo = False 
            break 
            
    if e_primo:
        print("esse numero é primo")
    else:
        print("esse numero não é primo")