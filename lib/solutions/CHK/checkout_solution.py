import numpy as np

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    
    arr = np.zeros((26,1))
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cost = [50, 30, 20, 15, 40, 10, 20, 10, 35]
    
    #verify for repeated elements
    for cha in skus:
        
        if cha in alphabet:
            idx_letter = alphabet.find(cha)
            arr[idx_letter] = arr[idx_letter] + 1
        else:
            return -1 
    
    #Offer E
    nbr_off_e = e//2
    if b>0:
        b = b - nbr_off_e
    cost_e = e * 40
    
    #Offer A
    nbr_off_a5 = a//5
    after_a5 = a - nbr_off_a5*5
    nbr_off_a3 = after_a5//3
    single_a = after_a5 - nbr_off_a3*3 
    cost_a = nbr_off_a5*200 + nbr_off_a3*130 + single_a*50
    
    #Offer B
    nbr_off_b = b//2 
    single_b = b - nbr_off_b*2 
    cost_b = nbr_off_b*45 + single_b*30
    
    
    cost_c = c * 20
    cost_d = d * 15
    
    #Offer F
    nbr_off_f = f//3
    f = f - nbr_off_f
    cost_f = f * 10
    
    
    #add total cost
    tcost = 0
    for i in range(0,26):
        #Offer E
        if i == 4:
        #Offer A
        elif i == 0:
        #Offer B
        elif i == 1:
        #Offer F
        elif i == 5:
        #Offer H
        elif i == 7:
        #Offer K
        elif i == 10:
        #Offer H
        elif i == 7:
        else:
            tcost = 
    
        
    return tcost
    
#out = checkout("EE")
#print(out)
##




