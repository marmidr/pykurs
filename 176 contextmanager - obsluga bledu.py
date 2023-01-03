import os
import zipfile
import requests

class FileFromWeb:
    def __init__(self, url, tmp_file):
        self.url = url
        self.tmp_file = tmp_file

    def __enter__(self):
        response = requests.get(self.url)
        with open(self.tmp_file, 'wb') as f:
            f.write(response.content)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('>>>>>>>>>>> Error details:', exc_type, exc_val, exc_tb)
        if exc_type == KeyError:
            print('>>>>> There is no file in archive! {}'.format(exc_val))
            return True # wyjątek obsłużony
        elif exc_type == FileNotFoundError:
            print('>>>>> Incorrect directory/file: {}'.format(exc_val))
            return  True
        else:
            return False # wyjątek nieobsłużony -> zrób to sam


with FileFromWeb('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip', '/tmp/euroxref.zip') as f:
    with zipfile.ZipFile(f.tmp_file, 'r') as z:
        print(z.namelist())
