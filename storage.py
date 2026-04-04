import argparse
import json
import os
import tempfile

# путь к файлу
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

# аргументы
parser = argparse.ArgumentParser()
parser.add_argument('--key')
parser.add_argument('--val')

args = parser.parse_args()

# читаем данные
if os.path.exists(storage_path):
    with open(storage_path, 'r') as f:
        data = json.load(f)
else:
    data = {}

# если есть значение  сохраняем
if args.val is not None:
    if args.key in data:
        data[args.key].append(args.val)
    else:
        data[args.key] = [args.val]

    with open(storage_path, 'w') as f:
        json.dump(data, f)

# если только ключ → читаем
else:
    values = data.get(args.key, [])
    print(', '.join(values))