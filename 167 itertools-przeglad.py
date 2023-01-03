import itertools as it

# Liczba doskonała – liczba naturalna, która jest sumą wszystkich swych
# dzielników właściwych (to znaczy od niej mniejszych).
# No to poszukajmy liczb doskonałych w przedziale od 1 - 10000.

def get_factors(x):
    ret_list = []
    for i in range(1, x):
        if x % i == 0:
            ret_list.append(i)
    return ret_list

print("dzielniki dla 20:")
print(get_factors(20))

candidate_list = list(range(1, 10001))
filtered_list = list(
    it.filterfalse(
        lambda x: x != sum(get_factors(x)),
        candidate_list
    )
)

print("liczby:")
for p in filtered_list:
    print(p, get_factors(p))
