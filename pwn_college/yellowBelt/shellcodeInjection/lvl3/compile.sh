#!/bin/bash


gcc -nostdlib -static shellcode.s -o shellcode-elf && objcopy --dump-section .text=shellcode-raw shellcode-elf
