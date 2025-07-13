import glob
import os

PWD = os.getcwd()
pattern = f'{PWD}/**/*.py'
query = 'backup'

for filepath in glob.iglob(pattern, recursive=True):
    try:
        with open(filepath, encoding='utf-8', errors='ignore') as f:
            for line in f:
                if query in line:
                    print(f'{filepath} => {line.strip()}')
                    break
    except Exception as e:
        print(f'HATA ({filepath}): {e}')