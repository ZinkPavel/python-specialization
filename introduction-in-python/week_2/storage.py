import argparse
import sys
import os
import json
import tempfile


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key')
    parser.add_argument('--val')

    return parser.parse_args(sys.argv[1:])


def read_data(file_path):
    if not os.path.exists(file_path):
        return dict()

    with open(file_path, 'r') as file:
        file_data = file.read()
        if file.tell() > 0:
            return json.loads(file_data)
        return dict()


def write_data(file_path, data):
    with open(file_path, 'w') as file:
        file.write(json.dumps(data))


def put(file_path, key, value):
    data = read_data(file_path)
    data[key] = data.get(key, list())
    data[key].append(value)
    write_data(file_path, data)


def get(file_path, key):
    data = read_data(file_path)
    return data.get(key, list())


def main(args, storage_path):
    if args.key and args.val:
        put(storage_path, args.key, args.val)
    elif args.key:
        print(*get(storage_path, args.key), sep=', ')
    else:
        print("The program is called with invalid parameters.")


if __name__ == '__main__':
    storage_path = os.path.join(tempfile.gettempdirb(), b'storage.data')
    args = parse_args()
    main(args, storage_path)
