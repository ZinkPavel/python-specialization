import argparse
import sys
import os
import json
import tempfile


my_dict = dict()
storage_path = os.path.join(tempfile.gettempdirb(), b'storage.data')

if not os.path.isfile(storage_path):
    os.system(f"touch {storage_path.decode('ascii')}")

with open(storage_path, 'r') as file:
    file_data = file.read()

    if file.tell() > 0:
        my_dict = json.loads(file_data)

if len(sys.argv) == 3:
    if not my_dict.get(sys.argv[2]):
        print(my_dict.get(sys.argv[2]))
    else:
        print(my_dict.get(sys.argv[2]))

if len(sys.argv) == 5:
    if not my_dict.get(sys.argv[2]):
        my_dict[sys.argv[2]] = list(sys.argv[4])
    else:
        my_dict[sys.argv[2]].append(sys.argv[4])

with open(storage_path, 'w') as file:
    file.write(json.dumps(my_dict))
