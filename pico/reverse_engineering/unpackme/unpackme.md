---
aliases: 
tags: 
category: ReverseEngineering
---

# PicoCTF: unpackme
Source link: (https://play.picoctf.org/practice/challenge/313?category=3&page=3)
# Write-up
Step 1, like always, is to download the binary.
`wget https://artifacts.picoctf.net/c/205/unpackme-upx`

Now that it's downloaded, let's see what we just downloaded.
`file *`
It's an ELF 64-bit LSB executable. Neat.

Now, I know that this CTF has something to do with being packed. So I'll open it in `vim` and search for `pack` in the strings and hope that I can figure out what packer they used to pack this binary. (The filename says they used `upx`, but let's verify just to be sure).
`vim unpackme-upx`
Yep, there it is on line 1,932. Awesome, now download that packer if you don't have it already. There's almost certainly an "unpack" option with the same tool. I already have it downloaded and installed, so I'll just continue.

If you just run `upx` by itself, it'll provide a very brief overview of the most common uses for this. Here, we see `upx -d filename` is what we want.
`upx -d unpackme-upx`
This unpacks the file in place. No new file will be created, it replaced our original. Woohoo.

Now, run `file` on the file again to see what's new.
`file unpackme-upx`
It's telling us that this is not stripped. Awesome, that tells us we have debugging information still available. That makes our job super easy now.

Open it up in `vim` again and see what we can find.
`vim unpackme-upx`

Hmm... Nothing too interesting seems to be going on here. Let's run the program and see what it does.
`chmod +x unpackme-upx`
`./unpackme-upx`

It's asking for us to enter the favorite number. Let's try 0, 1, and -1... Then a bunch of 1s, letters, combinations... 

Okay, well it handles the errors fairly and doesn't crash.
Let's rip this apart in Ghidra next, that should make quick work of this binary!

`ghidra`
Create a new project & import the binary. Run the analysis and open the listing view & the decompiled window, too. Then open the functions on the left side and search for the `main` function, if it doesn't automatically jump there for you.

Once we're viewing the `main` function in `Ghidra`,  we see the string there asking us to input the favorite number. That's probably what we want! We also see that it's comparing our input to `754653` in decimal. Let's run the program and enter that number, That'll be our next step in capturing this flag.
`./unpackme-upx`
`754653`

Wow, it's that easy. There's the flag. Enter that into pico and claim your reward.

# Flag

`picoCTF{up><_m3_f7w_5769b54e}`