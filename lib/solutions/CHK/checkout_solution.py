

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    #extract number of products
    a_idx = skus.find('A')
    
    if a_idx == -1:
        a = 0
    else:
        a = int(skus[0:a_idx])
        
    b_idx = skus.find('B')
    
    if b_idx == -1:
        b = 0
    else:
        b = int(skus[a_idx+1:b_idx])
        
    c_idx = skus.find('C')
        
    if c_idx == -1:
        c = 0
    else:
        c = int(skus[b_idx+1:c_idx])   
    
    d_idx = skus.find('D')
    
    if d_idx == -1:
        d = 0
    else:
        d = int(skus[c_idx+1:d_idx]) 
    
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
    
    print(total_cost)
    
    return total_cost
    
checkout("")
