# pwn.college | shellcode injection

This challenge asks us to remove all NULL bytes '0x00'

The trick here is to use XOR A, A to write a zero to a register.
Additionally, try to minimize the size of the registers used... If you only need to write 0x60, do you really need 64 bits to do that?

As before, I've created a bash script to compile the code for you. Just edit the 'shellcode.s' file.
