def run():
    l1 = [-1, 2, -3, 5, 7, 8, 9, -10]
    
    pos = lambda li1 : list(filter(lambda x : x >= 0, li1))
    neg = lambda li1 : list(filter(lambda x : x <  0, li1))
    print(pos(l1)+sorted(neg(l1)))
 

if __name__ == '__main__':
    run()