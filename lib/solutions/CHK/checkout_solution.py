

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    
    a = 0
    b = 0
    c = 0
    d = 0 
    
    #verify for repeated elements
    for cha in skus:
        if cha == 'A':
            a = a + 1
        if cha == 'B':
            b = b + 1
        if cha == 'C':
            c = c + 1
        if cha == 'D':
            d = d + 1
    
#    if ( (cnt_a > 1) or (cnt_b > 1) or (cnt_c > 1) or (cnt_d > 1)):
#        return -1
    
#    #extract number of products
#    a_idx = skus.find('A')
#    
#    if a_idx == -1:
#        a = 0
#    elif a_idx == 0:
#        a = 1
#    else:
#        a = int(skus[0:a_idx])
#        
#    b_idx = skus.find('B')
#    
#    if b_idx == -1:
#        b = 0
#    elif b_idx == 0:
#        b = 1
#    else:
#        b = int(skus[a_idx+1:b_idx])
#        
#    c_idx = skus.find('C')
#        
#    if c_idx == -1:
#        c = 0
#    elif c_idx == 0:
#        c = 1
#    else:
#        c = int(skus[b_idx+1:c_idx])   
#    
#    d_idx = skus.find('D')
#    
#    if d_idx == -1:
#        d = 0
#    elif d_idx == 0:
#        d = 1
#    else:
#        d = int(skus[c_idx+1:d_idx]) 
#    
#    print('A = '+str(a)+' B = '+str(b)+' C = '+str(c)+' D = '+str(d))
    
    nbr_offers_a = (a//3) 
    single_a = a - nbr_offers_a*3 
    cost_a = nbr_offers_a*130 + single_a*50
    
    nbr_offers_b = (b//2) 
    single_b = b - nbr_offers_b*2 
    cost_b = nbr_offers_b*45 + single_b*30
    
    cost_c = c * 20
    cost_d = d * 15
    
    total_cost = cost_a + cost_b + cost_c + cost_d
    
#    print(total_cost)
    
    return total_cost
    
#checkout("AxA")



