import json

def read_json(filepath):
    with open(filepath,'r') as f:
         return json.load(f)
         return
def write_json(data,filepath):
    with open(filepath, 'w') as f:
        return json.dump(data,f,indent=4)