import numpy as np

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    
    cnt = np.zeros((26,1))
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cost = [50, 30, 20, 15, 40, 10, 20, 10, 35]
    
    #verify for repeated elements
    for cha in skus:
        
        if cha in alphabet:
            idx_letter = alphabet.find(cha)
            cnt[idx_letter] = cnt[idx_letter] + 1
        else:
            return -1 
    
    #Offer A
    
    
    #Offer B
    nbr_off_b = b//2 
    single_b = b - nbr_off_b*2 
    cost_b = nbr_off_b*45 + single_b*30
    
    #Offer F
    nbr_off_f = f//3
    f = f - nbr_off_f
    cost_f = f * 10
    
    
    #add total cost
    tcost = 0
    for i in range(0,26):
        #Offer E
        if i == 4:
            nbr_off_e = cnt[4]//2
            if cnt[1]>0:
                cnt[1] = cnt[1] - nbr_off_e
            tcost = tcost + (cnt[i] * cost[i])
        #Offer N
        if i == 13:
            nbr_off_n = cnt[13]//3
            if cnt[12]>0:
                cnt[12] = cnt[12] - nbr_off_n
            tcost = tcost + (cnt[i] * cost[i])
        #Offer R
        if i == 17:
            nbr_off_r = cnt[17]//3
            if cnt[16]>0:
                cnt[16] = cnt[16] - nbr_off_r
            tcost = tcost + (cnt[i] * cost[i])
        #Offer A
        elif i == 0:
            nbr_off_a5 = a//5
            after_a5 = a - nbr_off_a5*5
            nbr_off_a3 = after_a5//3
            single_a = after_a5 - nbr_off_a3*3 
            cost_a = nbr_off_a5*200 + nbr_off_a3*130 + single_a*50
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
        #Offer P
        elif i == 15:
        #Offer Q
        elif i == 16:
        #Offer U
        elif i == 20:
        #Offer V
        elif i == 21:
        else:
            tcost = tcost + (cnt[i] * cost[i])
        
    return tcost
    
out = checkout("EE")
print(out)
#