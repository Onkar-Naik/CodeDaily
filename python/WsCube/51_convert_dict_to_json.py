"""
Write a python program to convert dictionary into json
"""
import json
a = {1:'One',2:'Two',3:'Three',4:'Four'}
print("Dictionary: ",a)
print(type(a))
b = json.dumps(a)
print("Json: ",b)
print(type(b))