def hp(d,mi,m):
    hp = d + (mi * m)
    print(hp)
    
hp(d = 5000, mi = 200, m = 10)




def alpha(sl,el,st): 
    for c in range(sl,el,st):
        yield chr(c)

print(set(alpha("d","t",2)))