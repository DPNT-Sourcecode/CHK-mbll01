

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    a_idx = skus.find('A')
    a_str = skus[0:a_idx]
    a = int(a_str)
    print(a)
    
    
checkout("1A20B5C0D")


