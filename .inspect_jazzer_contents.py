import os, zipfile, pathlib
path = pathlib.Path(os.getenv('TEMP')) / 'jazzer-junit-0.30.0.jar'
print('jar exists:', path.exists())
with zipfile.ZipFile(path) as z:
    names = [n for n in z.namelist() if n.startswith('com/code_intelligence/jazzer')]
    print('count:', len(names))
    print('\n'.join(names[:100]))
