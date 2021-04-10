import os

WORKING_PATH = '.'
FILES = []

def walk_dir(path):
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isfile(full_path):
            FILES.append(item)
        else:
            walk_dir(f'{path}/{item}')

walk_dir(WORKING_PATH)

print(FILES)