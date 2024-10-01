# TDE A

O seguinte projeto tem como objetivo comporar um codigo assembly nativo e um codigo assembly gerado por meio do minGW gcc windows 11.


## Como gerar o codigo assembly

Instalar previamente o gcc, se for windows instalar por meio do MinGW.

```shell
gcc -m32 -O3 -S -masm=intel nome_do_arquivo.c -o nome_do_arquivo.s
```