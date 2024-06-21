import os, sys, requests, bs4, re
from urllib.parse import urljoin

if len(sys.argv) != 2:
    sys.exit('使い方: python checkurl.py URL')

DIR = 'files'
os.makedirs(DIR, exist_ok=True)

url = sys.argv[1]

res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

links = soup.select('a')

href_set = set()

for link in links:
    href = link.get('href')
    if not href:
        continue

    if not href.startswith('http'):
        href = urljoin(url, href)

    href = re.sub(r'(#.+)', '', href)

    if href in href_set:
        continue
    href_set.add(href)
    print(href, end='', flush=True)
    
    try:
        res = requests.get(href)
        if res.status_code == 404:
            print(' -> 404 Not Found')
        elif res.status_code == 200:
            filename = re.sub(r'^(https?://)', '',href)
            filename = re.sub(r'[/~?&+]', '_', filename)
            hfile = open(os.path.join(DIR, filename), 'wb')
            for chunk in res.iter_content(100000):
                hfile.write(chunk)
            hfile.close()
            print('->', filename, 'に保存')
    except KeyboardInterrupt:
        print('\n中断しました')
        break
    except:
        print(' -> Error')
