"""
Write a python program to sort the json keys and print json data into a file
"""
import json
a = {"2":"Two","3":"Three","1":"One","4":"Four"}
b = json.dumps(a,indent=4,separators=(",","="),sort_keys=True)
f = open("demo.json","w")
f.write(b)