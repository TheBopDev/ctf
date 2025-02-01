---
aliases: 
tags: 
category: ReverseEngineering
---

# PicoCTF: FactCheck
Source link: (changeme)
# Write-up

First, let's get the file with *wget*.
`wget https://artifacts.picoctf.net/c_titan/188/bin`

## file
Great. Now we have the file in our directory... What is it? Let's next inspect it with *file*.
`file bin`
Gives us the result:
`bin: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=ed9d01aa375e575eb2cd16506aa83d6951841f87, for GNU/Linux 3.2.0, not stripped`
Okay, so we see it's an executable due to the ELF format. It's for x86 machines. And it's not stripped. This means there are still symbols, but no debug information.


## strings
Run the strings command on this and see what we get. Maybe we'll get lucky.
`strings bin`
We see `picoCTF{wELF_d0N3_mate_`
So that's the first half. Maybe we can just finish it with a `}` and run that.
Nope... That's not it. Let's keep marching forward. Open the file in `vim` to see if we can find anything else.

## vim
`vim bin`
Hmm.. Well, we can verify that the previous string is in this file. Unfortunately, there isn't much information here besides that.
We need to disassemble this binary. I've got high hopes, since the binary isn't stripped according to our file command earlier.

## Ghidra
TODO

# Flag
Not yet finished, but we've got a start.
`picoCTF{wELF_d0N3_mate_`
