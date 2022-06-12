

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    #extract number of products
    a_idx = skus.find('A')
    a_str = skus[0:a_idx]
    a = int(a_str)
    
    b_idx = skus.find('B')
    b_str = skus[a_idx+1:b_idx]
    b = int(b_str)
    
    c_idx = skus.find('C')
    c_str = skus[b_idx+1:c_idx]
    c = int(c_str)
    
    d_idx = skus.find('D')
    d_str = skus[c_idx+1:d_idx]
    d = int(d_str)
    
    print('A = '+str(a)+' B = '+str(b)+' C = '+str(c)+' D = '+str(d))
    
    
    
    
checkout("1A20B5C0D")



