import json, tempfile
with tempfile.NamedTemporaryFile() as f:
    f.write(b'{"text": "success"}'); f.flush()
    with open(f.name,'r') as lst:
        b = json.load(lst)
        print(b['text'])