# TDE A

O seguinte projeto tem como objetivo comporar um codigo assembly nativo e um codigo assembly gerado por meio do minGW gcc windows 11.

## Como gerar o codigo assembly

Instalar previamente o gcc, se for windows instalar por meio do MinGW.

Rodar o comando que gera assembly em release sem otimizações para intel 32bits
```shell
gcc -m32 -O0 -fno-builtin -S -masm=intel -fverbose-asm somvet.c -o somvet.asm
```
