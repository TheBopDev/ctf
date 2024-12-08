---
aliases: 
tags: 
category: ReverseEngineering
---

# PicoCTF: vault-door-training
Source link: (https://play.picoctf.org/practice/challenge/7?category=3&page=1)
# Write-up
First, let's download the source code.
`wget https://jupiter.challenges.picoctf.org/static/03c960ddcc761e6f7d1722d8e6212db3/VaultDoorTraining.java`

Inspect the file to see what we're working with.
`file VaultDoorTraining.java`

Neat. We see it's C++ source code, in plain ASCII text.
Let's open it up with a text editor. I'll use `vim`
`vim VaultDoorTraining.java`

I see two interesting things here.
1. Line 9 contains the first string of our flag.
2. Line 24 contains a password of some sort. Maybe that's the rest of our flag. 
I'll try to put the two together and submit that as the flag. Maybe that'll work.

Wow! It worked!

# Flag
`picoCTF{w4rm1ng_Up_w1tH_jAv4_3808d338b46}`