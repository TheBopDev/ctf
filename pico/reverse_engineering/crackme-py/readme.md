# __PICO CTF__ 
## _crackme-py_

 __Source__

> https://mercury.picoctf.net/static/2ff6c888060f14af5db1232e319547c9/crackme.py 

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Reverse | 30 | D20

**Description:** 

> crackme.py

## Solution
1. Make a new directory for this challenge.
	`mkdir crackme-py`
2. Download the source by using wget.
	`wget https://mercury.picoctf.net/static/2ff6c888060f14af5db1232e319547c9/crackme.py`
3. Vim into the file and see what we're working with... Immediately see `bezos_cc_secret` variable and `rotate_const = 47`.
4. Copy the variable into an online decoder and check the Rot47 decode... `https://dencode.com/en/`
5. Success! Key found.

> picoCTF{1|\/|_4_p34|\|ut_ef5b69a3}
