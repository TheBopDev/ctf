# __PICO CTF__ 
## _transformation_

 __Source__

> https://play.picoctf.org/practice/challenge/104?category=3&page=1 

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Reverse | 20 | D20

**Description:** 

> I wonder what this really is... enc ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

## Solution
1. Make a new directory for this challenge.
	`mkdir transformation`
2. Download the source by using wget.
	'wget https://mercury.picoctf.net/static/e47483f88b12f2ab0c46315afc12f64d/enc`
3. Attempt to vim into the file to see the source code... It's garbage characters.
4. Copy the characters into an online decoder.
	`https://dencode.com/en/`
5. No results... Change encoding standard to UTF-16, then UTF-32, etc and check for a flag.
6. Flag found using UTF-16 using Quoted-printable encoding.

### And this is subtitle
Text under the subtitle

> picoCTF{16_bits_inst34d_of_8_26684c20}
