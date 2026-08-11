import zipfile, pathlib, os
for p in pathlib.Path(os.getenv('TEMP')).glob('jazzer*.jar'):
    with zipfile.ZipFile(p) as z:
        matches=[n for n in z.namelist() if 'FuzzedDataProvider' in n]
        print(p.name, len(matches))
        if matches:
            print('\n'.join(matches))
