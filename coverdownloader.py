import requests
import os

os.makedirs('covers', exist_ok=True)

with open('list.txt', 'r') as f:
    codes = f.read().splitlines()


for code in codes:
    code = code.strip()
    if not code:
        continue
    
    url = f'https://raw.githubusercontent.com/xlenore/ps2-covers/main/covers/3d/{code}.png'
    filename = f'covers/{code}.png'
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f'{code}.png')
        else:
            print(f'not found: {code}')
    except Exception as e:
        print(f'error {code}: {e}')

print('done')