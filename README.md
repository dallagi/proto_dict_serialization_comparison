```bash
pip install -r requirements.txt

sh compile_proto.sh
sh compile_betterproto.sh

python proto_json.py
python betterproto_json.py
```

### Results

```bash
$ python proto_json.py 

Including default values: True
{'intValue': 10,
 'nestedMessage': {'floatValue': 3.14},
 'nonOptionalField': '5',
 'optionalField': ''}

Including default values: False
{'intValue': 10, 'nestedMessage': {'floatValue': 3.14}, 'nonOptionalField': '5'}


$ python betterproto_json.py 

Including default values: True
{'intValue': 10,
 'nestedMessage': {'boolValue': False, 'floatValue': 3.14},
 'nonOptionalField': '5',
 'optionalField': '',
 'stringValue': ''}

Including default values: False
{'intValue': 10, 'nestedMessage': {'floatValue': 3.14}, 'nonOptionalField': '5'}
```
