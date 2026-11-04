# Using


Copy this repository to the main folder.

```bash
git clone https://github.com/barstars/termux-pyvenv.git
```

After that, run pyvenv.py which is located inside termux-pyvenv, while you are in the main folder

```bash
python termux-pyvenv/pyvenv.py
```
After that, a venv folder will be created, and inside it, there will be .bash files

You can do them like this

```bash
source venv/[bash file]
```

Exemple:
```bash
source venv/create_venv.bash # creates a venv
```

## Bash file list
create_venv.bash - creates venv

activate_venv.bash - activate venv