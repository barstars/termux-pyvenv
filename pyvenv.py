import os
from pathlib import Path

def generate_venv_name(file_path):
    if (file_path[0] == "/"):
        file_path = file_path[1:]
    if (file_path[-1] == "/"):
        file_path = file_path[0:len(file_path)-1]
    return file_path.replace("/", "-")

def create_bash(venv_name):
    if not (os.path.exists("venv")):
        os.mkdir("venv")

    write_file(
        f"python -m venv ~/{venv_name}",
        "venv/create_venv.bash"
    )
    write_file(
        f"source ~/{venv_name}/bin/activate",
        "venv/activate_venv.bash"
    )

def write_file(text, file):
    with open(file, "w") as f:
        f.write(text)
        
def get_real_path():
    return "/storage/emulated/0"

def cdpath(path_all):
    # войдет до path_all папку
    path_list = path_all.split("/")
    for path in path_list:
        if (path != ""):
            os.chdir(path)

def get_file_path():
    absalute_path = str(Path.cwd())
    real_path = get_real_path()
    return absalute_path[len(real_path):]

file_path = get_file_path()
venv_name = generate_venv_name(file_path)
print(venv_name)

create_bash(venv_name)