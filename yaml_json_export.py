import yaml, json

mydict = {'Name': 'Bob', 'Age': 32, 'Occupation': 'IT Slave'}
mylist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, mydict]

with open("some_file.yaml", "w") as f:
    f.write(yaml.dump(mylist, default_flow_style=False))

with open("some_file.json", "w") as f:
    f.write(json.dumps(mylist, f))
