import pandas as pd
import json

def preprocess_each(key):
    return chr(ord(key) - 49)

def preprocess_key(key):
    if key == 'main':
        return
    return [preprocess_each(ch) for ch in list(key)]



data_path = r'D:\test\extensions\keys\basic.csv'
df = pd.read_csv(data_path)

result = {}

for i in range(len(df)):
    formated_keys = []
    row = df.iloc[i]
    quiz, keys = row[0], list(row[1:].dropna())
    for i in range(len(keys)):
        tmp = preprocess_key(keys[i])
        if not tmp:
            continue
        for t in tmp:
            formated_keys.append(f'question-{i}-{t}')
        
        result[quiz] = formated_keys

with open(r'D:\test\extensions\keys\basic.json', 'w') as f:
    json.dump(result, f)