import urllib3
import re
import pickle
http = urllib3.PoolManager()



link = "http://www.pythonchallenge.com/pc/def/banner.p"

result = http.request("GET",link)

obj = pickle.loads(result.data)

for element in obj:
    for x,y in element:
        print(x * y, end='')  
    print()
#channel
