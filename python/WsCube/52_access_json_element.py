"""
Write a python program to access json element
"""
import json
a = """{"1":"One","2":"Two","3":"Three","4":"Four"}"""
b = json.loads(a)
print(b["1"])