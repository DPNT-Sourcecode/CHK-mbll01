

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    
    a = 0
    b = 0
    c = 0
    d = 0 
    e = 0
    
    #verify for repeated elements
    for cha in skus:
        if cha == 'A':
            a = a + 1
        elif cha == 'B':
            b = b + 1
        elif cha == 'C':
            c = c + 1
        elif cha == 'D':
            d = d + 1
        elif cha == 'E':
            e = e + 1
        else:
            return -1 
        
    nbr_offers_e = e//2
    if b>0:
        b = b - nbr_offers_e
    cost_e = e * 40
    
    nbr_off_a5 = a//5
    after_a5 = a - nbr_off_a5*5
    nbr_off_a3 = after_a5//3
    single_a = after_a5 - nbr_off_a3*3 
    cost_a = nbr_off_a5*200 + nbr_off_a3*130 + single_a*50
    
    nbr_offers_b = b//2 
    single_b = b - nbr_offers_b*2 
    cost_b = nbr_offers_b*45 + single_b*30
    
    cost_c = c * 20
    cost_d = d * 15
    
    total_cost = cost_a + cost_b + cost_c + cost_d + cost_e
        
    return total_cost
    
#out = checkout("EE")
#print(out)
##



