ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

routes = [ (start, stop) for start in ports for stop in ports]
print(len(routes))

routes = [(start, stop)
            for start in ports
            for stop in ports
            if stop > start
        ]
print(len(routes))
