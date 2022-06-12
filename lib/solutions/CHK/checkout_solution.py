

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    #extract number of products
    a_idx = skus.find('A')
    b_idx = skus.find('B')
    c_idx = skus.find('C')
    d_idx = skus.find('D')
    
    if ( (a_idx == -1) or (b_idx == -1) or (c_idx == -1) or (d_idx == -1)):
        print("-1")
        return -1
    
    a = int(skus[0:a_idx])
    b = int(skus[a_idx+1:b_idx])
    c = int(skus[b_idx+1:c_idx])
    d = int(skus[c_idx+1:d_idx])
    
    print('A = '+str(a)+' B = '+str(b)+' C = '+str(c)+' D = '+str(d))
    
    nbr_offers_a = (a//3) 
    single_a = a - nbr_offers_a*3 
    cost_a = nbr_offers_a*130 + single_a*50
    
    nbr_offers_b = (b//2) 
    single_b = b - nbr_offers_b*3 
    cost_b = nbr_offers_b*45 + single_a*50
    
    
checkout("1A20B5C0D")






