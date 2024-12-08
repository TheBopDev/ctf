---
aliases: 
tags: 
category: ReverseEngineering
---

# PicoCTF: Packer
Source link: (https://play.picoctf.org/practice/challenge/421?category=3&page=1)
# Write-up
First, let's get the file.
`wget https://artifacts.picoctf.net/c_titan/103/out`

This results in downloading a file called `out`.
Run the typical inspection steps...
`file out`


Opening the file in `vim`, we can see on line 1619, this file is packed with `UPX`. It provides the source link and version information. Let's download that and see if there's a way to unpack...

`sudo pacman -S upx`
There's a package for it, so I installed it with this command.

Let's run `upx` by itself to see if there's a help window.
`upx`
```
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2024
UPX 4.2.4       Markus Oberhumer, Laszlo Molnar & John Reiser    May 9th 2024

Usage: upx [-123456789dlthVL] [-qvfk] [-o file] file..

Commands:
  -1     compress faster                   -9    compress better
  -d     decompress                        -l    list compressed file
  -t     test compressed file              -V    display version number
  -h     give more help                    -L    display software license
Options:
  -q     be quiet                          -v    be verbose
  -oFILE write output to 'FILE'
  -f     force compression of suspicious files
  -k     keep backup files
file..   executables to (de)compress

Type 'upx --help' for more detailed help.

UPX comes with ABSOLUTELY NO WARRANTY; for details visit https://upx.github.io
```

Excellent. We can just use the `-d` option to decompress. Let's run that now.
`upx -d out`

Running `ls -all` indicates the file name is the same, but the size is quite a bit larger.
Let's inspect this in `vim` again and see if there's anything interesting that jumps out at us now that this binary is unpacked.

`vim out`
It still looks like a mess at the head of this file. Let's run a cursory string search for `password`. In doing so, we see that on line 1123 there's ain interesting line. Copy and paste that long string `7069636f4354467b5539585f556e5034636b314e365f42316e34526933535f36666639363465667d` and throw it into cyberchef, from hex.

Wow, that was easy. Now we have the flag. See below :)
# Flag
`picoCTF{U9X_UnP4ck1N6_B1n4Ri3S_6ff964ef}`