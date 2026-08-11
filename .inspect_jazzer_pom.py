import pathlib, urllib.request
url = 'https://repo1.maven.org/maven2/com/code-intelligence/jazzer-junit/0.30.0/jazzer-junit-0.30.0.pom'
text = urllib.request.urlopen(url).read().decode('utf-8')
print(text)
