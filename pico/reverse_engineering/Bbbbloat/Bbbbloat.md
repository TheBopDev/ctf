---
aliases: 
tags: 
category: ReverseEngineering
---

# PicoCTF: Bbbbloat
Source link: (changeme)
# Write-up
The first think you should do is download the file.
`wget https://artifacts.picoctf.net/c/46/bbbbloat`
Let's see what it is with `file`
`file *`

Looks like it's a stripped ELF file. Great. Open it in `vim` just to see if we can get an easy win.
`vim bbbbloat`

Hmm... Doesn't look fruitful. Let's exit this and just run the program.
`chmod +x bbbbloat` (first, make the file executable)
`./bbbbloat`

It's asking for a number. Try -1, 0, and 1. Then a few letters... Hmm, it's not breaking. I think it's time to fire up Ghidra and really dig into this.
`ghidra`

After searching around for a while, exploring each of the functions, we see one called `FUN_00101307`. This function contains the string we saw when we ran the executable. It's also showing us that the `scanf` function is putting our value into `local_48`, and then immediately comparing `local_48` to a hard coded value... Convert that to decimal, and enter that as the "favorite number" in the executable.
`./bbbbloat`
`549255`

Boom, our flag is printed.

# Flag

`picoCTF{cu7_7h3_bl047_695036e3}`