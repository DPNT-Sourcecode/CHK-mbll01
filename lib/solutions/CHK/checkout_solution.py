import numpy as np

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    
    cnt = np.zeros((26))
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cost = [50, 30, 20, 15, 40, 10, 20, 10, 35, 60, 80, 90, 15, 40, 10, 50, 30, 50, 30, 20, 40, 50, 20, 90, 10, 50]
    
    #verify for repeated elements
    for cha in skus:
        if cha in alphabet:
            idx_letter = alphabet.find(cha)
            cnt[idx_letter] = cnt[idx_letter] + 1
        else:
            return -1 
    
    #add total cost
    tcost = 0
    for i in range(0,26):
        #Offer E
        if i == 4:
            tcost = tcost + offer_type_e(cnt[i],2,cost[i],cnt[1],cost[1])
        #Offer N
        elif i == 13:
            tcost = tcost + offer_type_e(cnt[i],3,cost[i],cnt[12],cost[12])
        #Offer R
        elif i == 17:
            tcost = tcost + offer_type_e(cnt[i],3,cost[i],cnt[16],cost[16])
        #Offer A
        elif i == 0:
            tcost = tcost + offer_type_a(cnt[i],5,200,3,130,cost[i])
        #Offer B
        elif i == 1:
            tcost = tcost + offer_type_b(cnt[i],2,45,30)
        #Offer F
        elif i == 5:
            tcost = tcost + offer_type_f(cnt[i],2+1,cost[i])
        #Offer H
        elif i == 7:
            tcost = tcost + offer_type_a(cnt[i],10,80,5,45,cost[i])
        #Offer K
        elif i == 10:
            tcost = tcost + offer_type_b(cnt[i],2,150,80)
        #Offer P
        elif i == 15:
            tcost = tcost + offer_type_b(cnt[i],5,200,50)
        #Offer Q
        elif i == 16:
            tcost = tcost + offer_type_b(cnt[i],3,80,30)
        #Offer U
        elif i == 20:
            tcost = tcost + offer_type_f(cnt[i],3+1,cost[i])
        #Offer V
        elif i == 21:
            tcost = tcost + offer_type_a(cnt[i],3,130,2,90,cost[i])
        else:
            tcost = tcost + (cnt[i] * cost[i])
        
    return tcost

def offer_type_a(cnt, bo, bop, so, sop, sp):
    nbr_off_bo = cnt//bo
    after_bo = cnt - (nbr_off_bo*bo)
    nbr_off_so = after_bo//so
    single_cnt = after_bo - nbr_off_so*so
    cost_type_a = nbr_off_bo*bop + nbr_off_so*sop + single_cnt*sp
    return cost_type_a

def offer_type_b(cnt,o,op,sp):
    nbr_off = cnt//o 
    single = cnt - nbr_off*o 
    cost_type_b = nbr_off*op + single*sp
    return cost_type_b

def offer_type_e(cnt,o,sp,cnto,spo):
    nbr_off = cnt//o
    if cnto>0:
        cost_type_e = (cnt * sp) - (nbr_off * spo)
    else:
        cost_type_e = cnt * sp
    return cost_type_e

def offer_type_f(cnt,o,sp):
    nbr_off = cnt//o
    cnt = cnt - nbr_off
    cost_type_f = cnt * sp
    return cost_type_f
    
out = checkout("E")
print(out)
#

