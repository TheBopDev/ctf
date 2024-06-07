# __PICO CTF__ 
## _information_

 __Source__

> https://play.picoctf.org/practice/challenge/186?category=4&page=1

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Forensics | 10 | D20

**Description:** 

> Files can always be changed in a secret way. Can you find the flag? `cat.jpg`

## Solution
1. Make a new directory... wget the file.
2. Run the `file` command to see what type of file it is. Maybe it's actually a plain text file just with a bad filename for obfuscation?... It appears to be actually be a JPEG image file.
3. Running `binwalk` to verify it's an image indicates it truly is an image.
4. For fun, try opening the file in `vim`... The license key looks interesting. Try throwing that in a decoder `https://dencode.com/en/`
5. They appear to have used base64 encoding to encrypt the key.
6. Success!!

> `picoCTF{the_m3tadata_1s_modified}`
