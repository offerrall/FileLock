# FileLock

A simple tool for encrypting and decrypting files.

## Usage

FileLock offers three commands for your file security needs:

- `lock`: encrypt a file
- `unlock`: decrypt a file
- `getkey`: generate a new encryption key

### lock

The `lock` command encrypts a file and requires two arguments:
- `file`: the path to the file to be encrypted
- `key`: the encryption key, or the path to the file containing the key

The encrypted file will be saved with the `.enc` extension and the path to it will be displayed.

### unlock

The `unlock` command decrypts a file and requires two arguments:
- `file`: the path to the file to be decrypted
- `key`: the encryption key, or the path to the file containing the key

The decrypted file will be saved with its original name, without the `.enc` extension.

### getkey

The `getkey` command generates a new encryption key and has one optional argument:
- `save` (default: `True`): whether to save the key to a file

If `save` is set to `True`, the key will be saved in a file named `key.txt` in the current directory and the path to the file will be displayed.

## Example

# Encrypt file.txt with the key in key.txt
python filelock.py lock file.txt key.txt

# Decrypt file.txt.enc with the key in key.txt
python filelock.py unlock file.txt.enc key.txt

# Generate a new key and save it to key.txt
python filelock.py getkey

# Generate a new key without saving it to a file
python filelock.py getkey --no-save


