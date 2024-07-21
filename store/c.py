import chardet

# Detect the encoding
with open('store/data.json', 'rb') as f:
    raw_data = f.read()
    result = chardet.detect(raw_data)
    encoding = result['encoding']

# Convert to UTF-8
with open('store/data.json', 'r', encoding=encoding) as f:
    data = f.read()

with open('store/data_utf8.json', 'w', encoding='utf-8') as f:
    f.write(data)
