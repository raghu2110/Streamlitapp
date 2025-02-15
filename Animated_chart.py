import pandas as pd
df = pd.read_csv('Formats/Data/employee-manager.csv', header=0).convert_dtypes()

import Formats
import json
root = Formats.getJson(df)
#print(root)

with open('templates/collapsible-tree.html', 'r') as file:
    content = file.read()

content = content.replace('"{{data}}"', json.dumps(root, indent=1))

import os
filename = os.path.abspath('Charts/collapsible-tree.html')
with open(filename, "w") as file:
    file.write(content)

import webbrowser
webbrowser.open('file://' + filename)