"""
Write a python program to pretty print json data
"""
import json
a = {"1":"One","2":"Two","3":"Three","4":"Four"}
b = json.dumps(a,indent=4,separators=(",","="))
print(b)