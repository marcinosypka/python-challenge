import urllib3
from collections import Counter
import re

def get_messy_string():   
    url = "http://www.pythonchallenge.com/pc/def/ocr.html"
    http = urllib3.PoolManager()
    r = http.request('GET',url)
    text = str(r.data.decode())

    return text.split('<!--')[2][:-5]

regex = re.compile("[A-Za-z]")
string = get_messy_string()
print(''.join(regex.findall(string)))
print(''.join([x for x,y in Counter(string).most_common()[-8:] ]))
#equality


    