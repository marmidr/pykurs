import os
import zipfile
import requests
import time

class FileFromWeb:
    def __init__(self, url, tmp_file):
        self.url = url
        self.tmp_file = tmp_file

    def __enter__(self):
        #download
        t = time.perf_counter()
        response = requests.get(self.url)
        t = time.perf_counter() - t
        print(f"Downloaded, took {t:4.3f}s")
        with open(self.tmp_file, 'wb') as f:
            f.write(response.content)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


with FileFromWeb('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip', '/tmp/euroxref.zip') as f:
    with zipfile.ZipFile(f.tmp_file, 'r') as z:
        print(z.namelist())
        a_file = z.namelist()[0]
        if not os.path.isdir('/tmp/eurofxref'): os.mkdir('/tmp/eurofxref')
        os.chdir('/tmp/eurofxref')
        z.extract(a_file, '.', None)
