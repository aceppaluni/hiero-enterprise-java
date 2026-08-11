import pathlib, urllib.request, zipfile, os
url = 'https://repo1.maven.org/maven2/com/code-intelligence/jazzer-junit/0.30.0/jazzer-junit-0.30.0.jar'
dest = pathlib.Path(os.getenv('TEMP')) / 'jazzer-junit-0.30.0.jar'
urllib.request.urlretrieve(url, dest)
with zipfile.ZipFile(dest, 'r') as z:
    print(z.read('META-INF/MANIFEST.MF').decode('utf-8'))
