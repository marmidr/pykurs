import os
import urllib.request
import urllib.error

data_dir = "/tmp/kurs_pobrane"

pages = [
    { 'name': 'mobilo',      'url': 'http://www.mobilo24.eu/'},
    { 'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/' },
    { 'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'}
]

if not os.path.isdir(data_dir):
    os.mkdir(data_dir)

for page in pages:
    path = os.path.join(data_dir, page['name']) + ".html"
    url = page['url']
    print("Pobieram ", path, "=>", url, "...")
    try:
        urllib.request.urlretrieve(url, path)
        print("...skonczone")
    except urllib.error.URLError as e:
        print(e)
    except Exception as e:
        print(e)
        break
else:
    print("Wszystko zostało pobrane")
