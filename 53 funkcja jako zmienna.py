def double(x):
    return 2 *x

def square(x):
    return x**2

def negative(x):
    return -x

def div2(x):
    return x/2

number = 8
transformations = [double, square, div2, negative]

print('Starting transformations for ', number)
tmp_return_value = number
for tr in transformations:
    tmp_return_value = tr(tmp_return_value)
    print('{:10}: temporal result is {}'.format(tr.__name__, tmp_return_value))

number = 125
transformations = [square, square, div2, double]

print('Starting transformations for ', number)
tmp_return_value = number
for tr in transformations:
    tmp_return_value = tr(tmp_return_value)
    print('{:10}: temporal result is {}'.format(tr.__name__, tmp_return_value))
