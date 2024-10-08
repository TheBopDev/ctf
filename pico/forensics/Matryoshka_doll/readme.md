# __PICO CTF__ 
## _Matryoshka doll_

 __Source__

> https://play.picoctf.org/practice/challenge/129?category=4&page=1

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Forensics | 30 | D20

**Description:** 

> `Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: this`

## Solution
1. `mkdir` for a new directory and `wget` the file.
2. First use `file` on the file to see what we're working with. Then use `binwalk` to see if there are any files stuck inside this one file.
3. We see there is a zip file inside... So, use the following command to extract all files within a file. `binwalk -D'.*' <file>.jpg`
4. `file` each of the new files to see what we got... One is a zip file, so `unzip` it.
5. Repeat steps 2-4 until we get to the bottom.
6. We see a file called `flag.txt`
7. `vim` into it and see if it's in plain text... It is, but not in the right format. So try to `cat flag.txt` next.
8. Success!

> `picoCTF{96fac089316e094d41ea046900197662}`
