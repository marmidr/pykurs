ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
            'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

# generator w zmiennej
routes_gen = ((start, stop) for start in ports for stop in ports)
print(routes_gen)

routes = [(start, stop) for start, stop in routes_gen]
print(type(routes))
print(len(routes))
# print(routes)

print('-' * 20)

routes_gen = ((start, stop)
            for start in ports
            for stop in ports
            if stop > start
)

routes = []

while True:
    try:
        a,b = next(routes_gen)
        routes.append((a,b))
    except StopIteration as e:
        break

print(len(routes))