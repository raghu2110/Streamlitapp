import pandas as pd
import json

def getJson(df):
    nodes = {}
    for _, row in df.iterrows():
        name = row.iloc[0]
        nodes[name] = {"name": name}
    root = None
    for _, row in df.iterrows():
        node = nodes[row.iloc[0]]
        isRoot = pd.isna(row.iloc[1])
        if isRoot:
            root = node 
        else:
            parent = nodes[row.iloc[1]]
            if "children" not in parent:
                parent["children"] = []
            parent["children"].append(node)
    return root

def getXml(data):
    pass

def getYaml(data):
    pass

df = pd.read_csv('Formats/Data/employee-manager.csv', header=0).convert_dtypes()

root = getJson(df)
with open('Formats/Data/employee-manager.json', 'w') as f:
    f.writelines(json.dumps(root,indent=2))

#root = getXml(df)
#with open('Formats/Data/employee-manager.xml', 'w') as f:
 #   f.writelines(root)

#root = getYaml(df)
#with open('Formats/Data/employee-manager.yaml', 'w') as f:
#    f.writelines(root)

