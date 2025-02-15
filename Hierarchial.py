import pandas as pd
import json

def get_json(df):
    nodes = {}
    root = None  # Ensure root is initialized

    # Create node dictionary
    for _, row in df.iterrows():
        name = row.iloc[0]
        nodes[name] = {"name": name}

    # Assign children to parents
    for _, row in df.iterrows():
        node = nodes[row.iloc[0]]
        if pd.isna(row.iloc[1]): 
            root = node  # Assign root if no manager
        else:
            parent = nodes.get(row.iloc[1])
            if parent:  # Ensure parent exists
                parent.setdefault("children", []).append(node)

    return root

# Read CSV file
df = pd.read_csv("Data/employee-manager.csv", header=None)

# Convert to JSON
root = get_json(df)

# ✅ Corrected JSON writing
if root:
    with open("Data/employee-manager1.json", "w") as f:
        f.write(json.dumps(root, indent=2))
else:
    print("⚠️ No root node found. Check your CSV file!")