days = ['mon','tue','wed','thu','fri','sat','sun']

#inicjujac zmienna workdays pamiętaj o copy()
workdays = days.copy()
workdays.remove('sat')
workdays.remove('sun')

print('days: ', days)
print('workdays: ', workdays)
workdays2 = days[:] # cały zakres -> kopia
print(id(days), id(workdays), id(workdays2))
