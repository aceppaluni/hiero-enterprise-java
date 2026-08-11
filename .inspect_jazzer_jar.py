import pathlib, urllib.request, zipfile, os
url = 'https://repo1.maven.org/maven2/com/code-intelligence/jazzer/0.30.0/jazzer-0.30.0.jar'
dest = pathlib.Path(os.getenv('TEMP')) / 'jazzer-0.30.0.jar'
urllib.request.urlretrieve(url, dest)
with zipfile.ZipFile(dest) as z:
    names = [n for n in z.namelist() if n.startswith('com/code_intelligence/jazzer')]
    print(len(names))
    print('\n'.join(names[:100]))
