import urllib3
from time import time
# def get_message():
#     http = urllib3.PoolManager()
#     response = http.request("GET","http://www.pythonchallenge.com/pc/def/equality.html")
#     text = str(response.data.decode())
#     return text.split("<!--")[1][:-4]

# with open("3.txt","w") as file:
#     file.write(get_message())

import re

file = open("3.txt","rt")
message = file.read()

regex = re.compile("[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]")

#without overlapping matches (good enough)
#print(''.join(regex.findall(message)))

regex2 = re.compile("(?<=[^A-Z][A-Z]{3})[a-z](?=[A-Z]{3}[^A-Z])")
print(''.join(regex2.findall(message)))

#with overlapping matches
current_index = 0

results = []
while True:
    match = regex.search(message,current_index)
    if match:
        results.append(match.group(1))
        current_index = match.start()+1
    else:
        break

#print(''.join(results))
file.close()

#linkedlist

def reduce_string(state:tuple,c:str):
    if state:
        upper_count, result, candidate = state
    else:
        upper_count = 0
        result = ''
        candidate = ''
    if c.islower():
        if upper_count == 3:
            if candidate:
                result += candidate
            candidate = c
        else:
            candidate = ''
        upper_count = 0
    elif c.isupper():
        upper_count += 1
    return upper_count, result, candidate

from functools import reduce

reduce_start = time()
result = reduce(reduce_string,message,())
reduce_end = time()

print("Reduce time: {:5.3f}".format(reduce_end - reduce_start))
print(result)
string = "AAAaAAAbAAAcAAAAdAAAAdAAA"
rx = re.compile("(?<=[^A-Z][A-Z]{3})[a-z](?=[A-Z]{3}[^A-Z])")
print(rx.findall(string))


regex_start = time()
ultimate_regex = re.compile("(?<![A-Z])[A-Z]{3}([a-z])(?=[A-Z]{3}(?![A-Z]))")
result = ultimate_regex.findall(message)
regex_end = time()
print("Ultimate Regex time: {:5.3f}".format(regex_end - regex_start))