from typer import Typer
from cryptography.fernet import Fernet
from pathlib import Path

def encrypt_decrypt_file(key: str, file_in: Path, file_out: Path, encrypt: bool = True):
    with open(file_in, "rb") as f:
        data = f.read()

    try:
        fernet = Fernet(key)
    except Exception as e:
        raise Exception("Invalid key")

    if encrypt:
        encrypted_data = fernet.encrypt(data)
    else:
        encrypted_data = fernet.decrypt(data)

    with open(file_out, "wb") as f:
        f.write(encrypted_data)

def check_valid_input(file: Path, key: str):
    if not file.exists():
        raise FileNotFoundError(f"{file} does not exist")

def check_key_from_file(key: str):
    check = Path(key)
    if not check.exists():
        return key
    
    with open(check, "r") as f:
        key = f.read()
    
    return key

app = Typer(help="The key can be a string or a path to a file containing the key")

@app.command()
def lock(file: Path, key: Path):
    """Encrypts a file with a key and saves with .enc extension."""
    
    check_valid_input(file, key)
    new_name = Path(file.name + ".enc")
    key = check_key_from_file(key)
    encrypt_decrypt_file(key, file, new_name)
    print(new_name.absolute())
    
    return 
    

@app.command()
def unlock(file: Path, key: Path):
    """Decrypts a file with a key and saves with the original name"""
    
    check_valid_input(file, key)
    new_name = file.name
    if file.name.endswith(".enc"):
        new_name = file.name[:-4]
    new_name = Path(new_name)
    key = check_key_from_file(key)
    encrypt_decrypt_file(key, file, new_name, encrypt=False)

@app.command()
def getkey(save: bool = True):
    """Generates a key"""
    key = Fernet.generate_key().decode("utf-8")

    if save:
        file_out = Path("key.txt")
        path_abs = file_out.absolute()
        with open(path_abs, "w") as f:
            f.write(key)
        print(f"Key saved in {path_abs}")
        return

    print(key)



if __name__ == "__main__":
    try:
        app()
    except Exception as e:
        print(e)