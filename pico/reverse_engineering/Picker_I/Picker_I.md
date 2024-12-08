---
aliases: 
tags: 
category: ReverseEngineering
---

# PicoCTF: Picker_I
Source link: (https://play.picoctf.org/practice/challenge/400?category=3&page=1)
# Write-up
Let's first start the instance so we have access to downloading the source code.

After starting the session, we can grab the link to download the file. 
`wget https://artifacts.picoctf.net/c/514/picker-I.py`

Great. Let's open it up in a text editor and see if there's anything interesting here.
`vim picker-I.py`
Line 75 looks like an interesting function... It's saying we need to create a `flag.txt` file in this directory. Let's do that now.
`touch flag.txt`

Reconnect to the machine that Pico spun up for you. Your information will be different from mine.
`nc ...`

Now, call the `win` function we found in the source code and see if that'll write the flag to our `flag.txt` file.
`win`

Well... It didn't write to the file, but it printed to the screen. Copy that into cyberchef and see the results. Maybe that's the flag.

It's that easy :)
# Flag
`picoCTF{4_d14m0nd_1n_7h3_r0ugh_6e04440d}`