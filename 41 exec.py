import os

walker = os.walk(os.path.join(os.curdir, "41"))
# for root, dirs, files in walker:
#     print(root, dirs, files)
_, _, scripts = next(walker)
print("Found scripts: ", scripts)

for s in scripts:
    path = os.path.join(os.curdir, "41", s)
    with open(path) as f:
        script = f.read()
        print(f"Executing {path}...")
        exec(script)

