import urllib3
import re
http = urllib3.PoolManager()



link = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}"
next = 12345
regex = re.compile('\d+')

while next is not None:
    response = http.request("GET",link.format(next))
    text = response.data.decode('utf-8')
    print(text)
    result = regex.findall(text)
    if len(result) > 0:
        next = result[len(result)-1]
    elif text == "Yes. Divide by two and keep going.":
        next = int(next) / 2
#peak.html
