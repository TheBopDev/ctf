---
aliases: 
tags: 
category: ReverseEngineering
---

# PicoCTF: ASCII FTW
Source link: (changeme)
# Write-up
Step 1 as usual, download the file in question.
`wget https://artifacts.picoctf.net/c/506/asciiftw`

Step to, again like usual, run `file` against the downloaded file to see what we're working wtih.
`file asciiftw`

We see it's a 64-bit ELF and it's not stripped. That means we have debugging information. That makes our job much easier! Yay.

Let's see what we can figure out by opening the file up in `vim`.
`vim asciiftw`

Hmm.. Not much. Let's just try running the file and see what happens.
`chmod +x asciiftw`
`./asciiftw`

Interesting. We are told that the flag begins with 70. Maybe try running `./asciiftw 70` and pass that as the argument.


Looking at the file in `Ghidra`, we see the following..
```
      00101184 c6 45 d0      MOV       byte ptr [RBP + local_38],0x70
               70
      00101188 c6 45 d1      MOV       byte ptr [RBP + local_37],0x69
               69
      0010118c c6 45 d2      MOV       byte ptr [RBP + local_36],0x63
               63
      00101190 c6 45 d3      MOV       byte ptr [RBP + local_35],0x6f
               6f
      00101194 c6 45 d4      MOV       byte ptr [RBP + local_34],0x43
               43
      00101198 c6 45 d5      MOV       byte ptr [RBP + local_33],0x54
               54
      0010119c c6 45 d6      MOV       byte ptr [RBP + local_32],0x46
               46
      001011a0 c6 45 d7      MOV       byte ptr [RBP + local_31],0x7b
               7b
      001011a4 c6 45 d8      MOV       byte ptr [RBP + local_30],0x41
               41
      001011a8 c6 45 d9      MOV       byte ptr [RBP + local_2f],0x53
               53
      001011ac c6 45 da      MOV       byte ptr [RBP + local_2e],0x43
               43
      001011b0 c6 45 db      MOV       byte ptr [RBP + local_2d],0x49
               49
      001011b4 c6 45 dc      MOV       byte ptr [RBP + local_2c],0x49
               49
      001011b8 c6 45 dd      MOV       byte ptr [RBP + local_2b],0x5f
               5f
      001011bc c6 45 de      MOV       byte ptr [RBP + local_2a],0x49
               49
      001011c0 c6 45 df      MOV       byte ptr [RBP + local_29],0x53
               53
      001011c4 c6 45 e0      MOV       byte ptr [RBP + local_28],0x5f
               5f
      001011c8 c6 45 e1      MOV       byte ptr [RBP + local_27],0x45
               45
      001011cc c6 45 e2      MOV       byte ptr [RBP + local_26],0x41
               41
      001011d0 c6 45 e3      MOV       byte ptr [RBP + local_25],0x53
               53
      001011d4 c6 45 e4      MOV       byte ptr [RBP + local_24],0x59
               59
      001011d8 c6 45 e5      MOV       byte ptr [RBP + local_23],0x5f
               5f
      001011dc c6 45 e6      MOV       byte ptr [RBP + local_22],0x33
               33
      001011e0 c6 45 e7      MOV       byte ptr [RBP + local_21],0x43
               43
      001011e4 c6 45 e8      MOV       byte ptr [RBP + local_20],0x46
               46
      001011e8 c6 45 e9      MOV       byte ptr [RBP + local_1f],0x34
               34
      001011ec c6 45 ea      MOV       byte ptr [RBP + local_1e],0x42
               42
      001011f0 c6 45 eb      MOV       byte ptr [RBP + local_1d],0x46
               46
      001011f4 c6 45 ec      MOV       byte ptr [RBP + local_1c],0x41
               41
      001011f8 c6 45 ed      MOV       byte ptr [RBP + local_1b],0x44
               44
      001011fc c6 45 ee      MOV       byte ptr [RBP + local_1a],0x7d
               7d

```


That's probably our flag, except the values are in hex. I'll just manually convert these since there aren't that many, and I already know the first 8 characters are "picoCTF{" and the last character is "}". 

After converting the data, this is the following we get:
```
      00101184 c6 45 d0      MOV       byte ptr [RBP + local_38],'p'
               70
      00101188 c6 45 d1      MOV       byte ptr [RBP + local_37],'i'
               69
      0010118c c6 45 d2      MOV       byte ptr [RBP + local_36],'c'
               63
      00101190 c6 45 d3      MOV       byte ptr [RBP + local_35],'o'
               6f
      00101194 c6 45 d4      MOV       byte ptr [RBP + local_34],'C'
               43
      00101198 c6 45 d5      MOV       byte ptr [RBP + local_33],'T'
               54
      0010119c c6 45 d6      MOV       byte ptr [RBP + local_32],'F'
               46
      001011a0 c6 45 d7      MOV       byte ptr [RBP + local_31],'{'
               7b
      001011a4 c6 45 d8      MOV       byte ptr [RBP + local_30],'A'
               41
      001011a8 c6 45 d9      MOV       byte ptr [RBP + local_2f],'S'
               53
      001011ac c6 45 da      MOV       byte ptr [RBP + local_2e],'C'
               43
      001011b0 c6 45 db      MOV       byte ptr [RBP + local_2d],'I'
               49
      001011b4 c6 45 dc      MOV       byte ptr [RBP + local_2c],'I'
               49
      001011b8 c6 45 dd      MOV       byte ptr [RBP + local_2b],'_'
               5f
      001011bc c6 45 de      MOV       byte ptr [RBP + local_2a],'I'
               49
      001011c0 c6 45 df      MOV       byte ptr [RBP + local_29],'S'
               53
      001011c4 c6 45 e0      MOV       byte ptr [RBP + local_28],'_'
               5f
      001011c8 c6 45 e1      MOV       byte ptr [RBP + local_27],'E'
               45
      001011cc c6 45 e2      MOV       byte ptr [RBP + local_26],'A'
               41
      001011d0 c6 45 e3      MOV       byte ptr [RBP + local_25],'S'
               53
      001011d4 c6 45 e4      MOV       byte ptr [RBP + local_24],'Y'
               59
      001011d8 c6 45 e5      MOV       byte ptr [RBP + local_23],'_'
               5f
      001011dc c6 45 e6      MOV       byte ptr [RBP + local_22],'3'
               33
      001011e0 c6 45 e7      MOV       byte ptr [RBP + local_21],'C'
               43
      001011e4 c6 45 e8      MOV       byte ptr [RBP + local_20],'F'
               46
      001011e8 c6 45 e9      MOV       byte ptr [RBP + local_1f],'4'
               34
      001011ec c6 45 ea      MOV       byte ptr [RBP + local_1e],'B'
               42
      001011f0 c6 45 eb      MOV       byte ptr [RBP + local_1d],'F'
               46
      001011f4 c6 45 ec      MOV       byte ptr [RBP + local_1c],'A'
               41
      001011f8 c6 45 ed      MOV       byte ptr [RBP + local_1b],'D'
               44
      001011fc c6 45 ee      MOV       byte ptr [RBP + local_1a],'}'
               7d

```

That's very easy to work with. Toss that into a `vim` file, grab that column of characters, then paste it out. Ezpz.
# Flag

`picoCTF{ASCII_IS_EASY_3CF4BFAD}`