import os
import itertools


def scantree(path):
    # https://docs.python.org/3/library/os.html#os.scandir
    for entry in os.scandir(path):
        if entry.is_dir():
            yield entry
            yield from scantree(entry.path)
        else:
            yield entry

# listing = scantree('/bin')
# for l in listing:
#     print('DIR ' if l.is_dir() else 'FILE', l.path)


listing = scantree('/tmp')
listing = sorted(listing, key=lambda e: e.is_dir())

# iterator po listach pogrpowanych wg podanego klucza (tutaj: czy katalog)
for is_dir, elements in itertools.groupby(listing, key=lambda e: e.is_dir()):
    print('DIR ' if is_dir else 'FILE', len(list(elements)))
