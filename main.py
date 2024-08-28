list=[1,2,3,4,5,5,66,2,3,0]
sample_set=set(list)
print(sample_set)

if 100 in sample_set :
    print('number exist')
else:
    print('not there')

empty = set([])
empty.add(1)
empty.add(6)
empty.add(3)
empty.add(5)

print(empty)

empty.remove(1)

print(empty)

#if you remove number that's not there =ERROR
# if you discard a number that's not there = no ERROR
empty.discard(5)
print(empty)

#union, intersection,difference, symmetric difference

A = {1,2,3,4,5}
B = {4,5,6,7,8}

print("set A : ",A)
print("set B : ", B)

#union
print(A.union(B))
print(A|B)

#intersection
print(A&B)
print(A.intersection(B))

#difference
print(A-B)
print(A.difference(B))

print(B-A)

#sym difference (removes common terms)
print(A^B)
print(A.symmetric_difference(B))
