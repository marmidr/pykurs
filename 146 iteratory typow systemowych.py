import csv

with open('/proc/cpuinfo', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter='\t')
#    for row in csvreader:
#        print('|'.join(row))
    while True:
        try:
            data = next(csvreader)
            print(data)
        except StopIteration:
            break
    print('All data was processed')

# iterowanie przez tuple
print("---------")
tup = (1,False,"tak")
for x in tup: print(x)

print("---------")
# tuple nie jest iterable, bo nie ma __next__
#print(next(tup))
it = iter(tup)
print(next(it)) # teraz ok

# iterowanie przez set
print("---------")
simpleset = {3.1415, True, (-1,2), True}
for x in simpleset: print(x)
