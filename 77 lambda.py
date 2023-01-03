import sys

# sys.version_info(major=3, minor=8, micro=2, releaselevel='final', serial=0)
print(sys.version_info)

f = lambda x: len(x)

print(f('a 19-letters string'))

text_list = ['x','xxx','xxxxx','xxxxxxx','']

# v1
print(list(map(f, text_list)))
# v2
lengths = map(f, text_list)
print([x for x in lengths])
# v3
print([x for x in map(f, text_list)])
# v4 inline lambda
print(list(map(lambda s: len(s), text_list)))