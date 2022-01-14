#string permutation and Combination 

from itertools import permutations, combinations, combinations_with_replacement

li1 = [1,2,3]
per = list(permutations(li1, 3))
for i in per:
    print(i)
    pass

com = combinations(li1, 2)
for i in com:
    print(i)
    pass

comrem = combinations_with_replacement(li1, 2)
for i in comrem:
    print(i)
    pass


