	.file	"somvet.c"
	.intel_syntax noprefix
	.text
	.p2align 4,,15
	.globl	_somaVetor
	.def	_somaVetor;	.scl	2;	.type	32;	.endef
_somaVetor:
LFB0:
	.cfi_startproc
	push	ebx
	.cfi_def_cfa_offset 8
	.cfi_offset 3, -8
	mov	eax, DWORD PTR [esp+12]
	test	eax, eax
	jle	L4
	mov	edx, DWORD PTR [esp+8]
	lea	ebx, [edx+eax*2]
	xor	eax, eax
	.p2align 4,,10
L3:
	movsx	ecx, WORD PTR [edx]
	add	edx, 2
	add	eax, ecx
	cmp	ebx, edx
	jne	L3
	pop	ebx
	.cfi_remember_state
	.cfi_restore 3
	.cfi_def_cfa_offset 4
	ret
L4:
	.cfi_restore_state
	xor	eax, eax
	pop	ebx
	.cfi_restore 3
	.cfi_def_cfa_offset 4
	ret
	.cfi_endproc
LFE0:
	.def	___main;	.scl	2;	.type	32;	.endef
	.section	.text.startup,"x"
	.p2align 4,,15
	.globl	_main
	.def	_main;	.scl	2;	.type	32;	.endef
_main:
LFB1:
	.cfi_startproc
	push	ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	mov	ebp, esp
	.cfi_def_cfa_register 5
	and	esp, -16
	call	___main
	xor	eax, eax
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE1:
	.ident	"GCC: (MinGW.org GCC-6.3.0-1) 6.3.0"
