---
aliases: 
tags: 
category:
---

# PicoCTF: CanYouSee
Source link: (https://play.picoctf.org/practice/challenge/408?category=4&page=1)
# Write-up
Let's first get the file with `wget`.
`wget https://artifacts.picoctf.net/c_titan/130/unknown.zip`

What did we just download? Check it out with `file`
`file *`

Ahh, it's a zip folder. Unzip it with `unzip`
`unzip unknown.zip`

It produced a file called: `ukn_reality.jpg`
Inspect it again using the same file command from earlier. `file ukn_reality.jpg`

Open it in `vim` to see its contents. The image itself probably isn't even worth looking at.
`vim ukn_reality.jpg`

That's an interesting string I see on attribution URL. `cGljb0NURntNRTc0RDQ3QV9ISUREM05fNmE5ZjVhYzR9Cg==`
It's almost certainly a base64 encoded string (due to the two = at the end). Let's decode it using https://www.base64decode.org/

That gave us the flag :)
# Flag
picoCTF{ME74D47A_HIDD3N_6a9f5ac4}