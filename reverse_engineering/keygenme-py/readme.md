# __PICO CTF__ 
## _keygenme-py_

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Reverse | 30 | D20

**Description:** 

> keygenme-trial.py

## Solution
1. Make a directory for the new challenge. `mkdir keygenme-py`
2. Download the provided file. `wget https://mercury.picoctf.net/static/fb75b48f9214cf992a2199b5785564e7/keygenme-trial.py`
3. Try using `strings` and `file` commands on the file to get more info... Part of the key found!
4. Try to vim into the file and see what the source code says about the key... Look at `check_key` function.
5. See the key[i]... Create a new python script, called `keygen.py` calling	the function `hashlib.sha256(username_trial).hexdigest()[i]` in corresponding order and print it out. See if that's the key?
6. Success!


## Flag
> `picoCTF{1n_7h3_|<3y_of_0d208392}`
