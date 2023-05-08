import os

def CountWords(path):
    with open(path, 'r', encoding='utf-8', buffering=10) as f:
        content = f.read()
        words = content.split()
        word_count = len(words)
        lines = content.splitlines()
    return (word_count, len(lines))

path = r'05 id.py'
path = os.path.join(os.curdir, path)

if os.path.isfile(path):
    print("There are {} words/lines in the file '{}'".format(CountWords(path), path))

# os.path.isfile(path) and print("There are {} words in the file {}".format(CountWords(path), path))
os.path.isfile(path) and print(f"Words/lines: {CountWords(path)}")
