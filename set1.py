E={1,23,45,12,90,27}
N={1,9,23,78,34,56}
print("E U N:",E.union(N))#union of two sets
print(dir(set))#to find out different types of functions in sets
print(E.intersection(N))#common between the two sets
print(E.difference(N))#removal of all the common entites from E
print(N.difference(E))#removal of all the common entites from N
print(E.symmetric_difference(N))#printing of all the different entites except the common ones