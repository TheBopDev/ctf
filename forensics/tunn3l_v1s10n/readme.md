# __PICO CTF__ 
## _tunn3l v1s10n_

 __Source__

> https://play.picoctf.org/practice/challenge/112?category=4&page=1

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Forensics | 40 | D20

**Description:** 

> We found this file. Recover the flag.

## Solution
1. As always, `mkdir` a new working directory. `cd` into it and then `wget` the file.
2. Running `file tunn3l_v1s10n` produces an interesting output of: `tunn31_v1s10n: data`... Strange.
3. Trying to `hexdump -C tunn31_v1s10n | less` doesn't produce any meaningful information. Maybe try `exiv2 tunn31_v1s10n`?... Interesting, we find some more information.

> picoCTF{FLAG}
