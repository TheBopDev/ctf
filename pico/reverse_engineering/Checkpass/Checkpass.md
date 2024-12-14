---
aliases: 
tags: 
category: ReverseEngineering
---

# PicoCTF: Checkpass
Source link: (https://play.picoctf.org/practice/challenge/149?category=3&page=6)
# Write-up
Step 1 is always the same. Download the file.
`wget https://mercury.picoctf.net/static/beef707896b55295ef881fec2ae3490b/checkpass`

Step 2 is always the same, too.. Check it out with `file` and see what we're working with.
`file checkpass`
We see it's a stripped ELF x86 binary. Not as easy as some of the others, but let's throw it into `Ghidra` and see what we can determine :)

`Ghidra`


#### Trying to guess the password
Ghidra didn't immediately yield results like I was expecting (since the file is stripped).
Let's just try to run the file and guess the password.
`chmod +x checkpass`
`./checkpass password`
Start with 1 character and keep adding another character until the "Invalid  length" string goes away and it gives us our next hint...

`./password lllllllllllllllllllllllllllllllllllllllll` did the trick for me.
This shows us "Invalid password". So now we know the password length is 41, or `0x29` in hex.

Now, back to Ghidra.. If we look around some more, we can see that `FUN_00105960` compares `0x29` to something. That's likely the function we want to keep looking at.

# Flag