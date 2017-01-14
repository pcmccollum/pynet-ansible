import yaml, json
from pprint import pprint as pp

with open("some_file.yaml") as f:
    json_list = yaml.load(f)

with open("some_file.json") as f:
    yaml_list = yaml.load(f)
    
with open("pp.yaml", "w") as f:
    pp(yaml_list, stream=f)

with open("pp.json", "w") as f:
    pp(json_list, stream=f)

