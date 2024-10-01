	.file	"somvet.c"
	.intel_syntax noprefix
 # GNU C11 (MinGW.org GCC-6.3.0-1) version 6.3.0 (mingw32)
 #	compiled by GNU C version 6.3.0, GMP version 6.1.2, MPFR version 3.1.5, MPC version 1.0.3, isl version 0.15
 # GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
 # options passed:  -iprefix c:\mingw\bin\../lib/gcc/mingw32/6.3.0/
 # somvet.c -m32 -masm=intel -mtune=generic -march=i586
 # -auxbase-strip somvet_gerado.asm -O0 -fverbose-asm
 # options enabled:  -faggressive-loop-optimizations
 # -fasynchronous-unwind-tables -fauto-inc-dec -fchkp-check-incomplete-type
 # -fchkp-check-read -fchkp-check-write -fchkp-instrument-calls
 # -fchkp-narrow-bounds -fchkp-optimize -fchkp-store-bounds
 # -fchkp-use-static-bounds -fchkp-use-static-const-bounds
 # -fchkp-use-wrappers -fcommon -fdelete-null-pointer-checks
 # -fdwarf2-cfi-asm -fearly-inlining -feliminate-unused-debug-types
 # -ffunction-cse -fgcse-lm -fgnu-runtime -fgnu-unique -fident
 # -finline-atomics -fira-hoist-pressure -fira-share-save-slots
 # -fira-share-spill-slots -fivopts -fkeep-inline-dllexport
 # -fkeep-static-consts -fleading-underscore -flifetime-dse
 # -flto-odr-type-merging -fmath-errno -fmerge-debug-strings -fpeephole
 # -fplt -fprefetch-loop-arrays -freg-struct-return
 # -fsched-critical-path-heuristic -fsched-dep-count-heuristic
 # -fsched-group-heuristic -fsched-interblock -fsched-last-insn-heuristic
 # -fsched-rank-heuristic -fsched-spec -fsched-spec-insn-heuristic
 # -fsched-stalled-insns-dep -fschedule-fusion -fsemantic-interposition
 # -fset-stack-executable -fshow-column -fsigned-zeros
 # -fsplit-ivs-in-unroller -fssa-backprop -fstdarg-opt
 # -fstrict-volatile-bitfields -fsync-libcalls -ftrapping-math
 # -ftree-cselim -ftree-forwprop -ftree-loop-if-convert -ftree-loop-im
 # -ftree-loop-ivcanon -ftree-loop-optimize -ftree-parallelize-loops=
 # -ftree-phiprop -ftree-reassoc -ftree-scev-cprop -funit-at-a-time
 # -funwind-tables -fverbose-asm -fzero-initialized-in-bss -m32 -m80387
 # -m96bit-long-double -maccumulate-outgoing-args -malign-double
 # -malign-stringops -mavx256-split-unaligned-load
 # -mavx256-split-unaligned-store -mfancy-math-387 -mfp-ret-in-387
 # -mieee-fp -mlong-double-80 -mms-bitfields -mno-red-zone -mno-sse4
 # -mpush-args -msahf -mstack-arg-probe -mstv -mvzeroupper

	.text
	.globl	_somaVetor
	.def	_somaVetor;	.scl	2;	.type	32;	.endef
_somaVetor:
LFB0:
	.cfi_startproc
	push	ebp	 #
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	mov	ebp, esp	 #,
	.cfi_def_cfa_register 5
	sub	esp, 16	 #,
	mov	DWORD PTR [ebp-8], 0	 # soma,
	mov	DWORD PTR [ebp-4], 0	 # i,
	jmp	L2	 #
L3:
	mov	eax, DWORD PTR [ebp-4]	 # i.0_6, i
	lea	edx, [eax+eax]	 # _7,
	mov	eax, DWORD PTR [ebp+8]	 # tmp94, vetor
	add	eax, edx	 # _9, _7
	movzx	eax, WORD PTR [eax]	 # _11, *_9
	cwde
	add	DWORD PTR [ebp-8], eax	 # soma, _12
	add	DWORD PTR [ebp-4], 1	 # i,
L2:
	mov	eax, DWORD PTR [ebp-4]	 # tmp95, i
	cmp	eax, DWORD PTR [ebp+12]	 # tmp95, elementos
	jl	L3	 #,
	mov	eax, DWORD PTR [ebp-8]	 # _15, soma
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE0:
	.def	___main;	.scl	2;	.type	32;	.endef
	.globl	_main
	.def	_main;	.scl	2;	.type	32;	.endef
_main:
LFB1:
	.cfi_startproc
	push	ebp	 #
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	mov	ebp, esp	 #,
	.cfi_def_cfa_register 5
	and	esp, -16	 #,
	sub	esp, 32	 #,
	call	___main	 #
	mov	WORD PTR [esp+18], 1	 # vetor,
	mov	WORD PTR [esp+20], 2	 # vetor,
	mov	WORD PTR [esp+22], 3	 # vetor,
	mov	WORD PTR [esp+24], 4	 # vetor,
	mov	WORD PTR [esp+26], 5	 # vetor,
	mov	DWORD PTR [esp+4], 5	 #,
	lea	eax, [esp+18]	 # tmp90,
	mov	DWORD PTR [esp], eax	 #, tmp90
	call	_somaVetor	 #
	add	eax, eax	 # tmp91
	mov	DWORD PTR [esp+28], eax	 # soma, tmp91
	mov	eax, 0	 # _10,
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE1:
	.ident	"GCC: (MinGW.org GCC-6.3.0-1) 6.3.0"
