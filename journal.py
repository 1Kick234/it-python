import os

def load(name):
    data = []
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename, "r") as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data

def save(name, data):
    filename = get_full_pathname(name)
    print(f"..... saving to {filename}")
    with open(filename, "w") as fout:
        for entry in data:
            fout.write(entry+"\n")

def add_entry(text, data):
    data.append(text)

def get_full_pathname(name):
    filename = os.path.abspath(os.path.join(".", "journals", f"{name}.jrn"))
    return filename