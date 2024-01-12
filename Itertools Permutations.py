
import itertools

S, k = input().split()
permutations = list(itertools.permutations(sorted(S), int(k)))
perm_list = [ ''.join(permutation) for permutation in permutations ]

for perm in perm_list:
	print(perm)
