def get_list_of_colors(colors: list, n: int):
    return colors[:n]

colors = ["red", "orange", "green", "violet", "blue", "yellow"]

for i in range(1, len(colors)+1):
    print(get_list_of_colors(colors, i))


definition = 'Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli. '

slicestart = definition.index('(')+1
slicestop = definition.index(')')
slice = definition[slicestart : slicestop]
print(slice)

lst = list(range(1, 10))
print(lst)
print(lst[::2]) # krok = 2
print(lst[1:4])
print(lst[3:])
print(lst[:-2])
print(lst[-1::-1]) # krok = -1 -> lista od tyłu