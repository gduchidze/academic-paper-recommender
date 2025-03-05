import os
import pandas as pd

json_file_path = 'data.json'

print("Step 1: Loading Dataset...")

df = pd.read_json(json_file_path, lines=True)
df_sample = df.sample(n=500, random_state=42)

print(f"Loaded {len(df_sample)} papers.")