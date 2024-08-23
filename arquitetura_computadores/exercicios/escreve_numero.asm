.model small

.stack 100H

.data
    numero  db ?
    acertos db 12
    tam     dw 45H
    lado    dw 67H    

.code

ESCREVE_CHAR proc
    push AX ;empilha reg para salvar valor
    mov AH, 2
    int 21H   
    pop AX ;desempilha reg
    ret
endp 

;escreve na tela o valor armazenado em AX
ESCREVE_INT16 proc    
    ;; AX=739     
    xor CX, CX  ;;zera contador 
    mov BX, 10  ;;adiciona o dezena para servir de divisor
    
    
LACO_DIGITO: 
    ;;pegar unidade
    xor DX, DX ;; reseta registrador com valor do decimal
    div BX; AX=73 DX=9
    
    ;;empilhar unidade
    push DX

    ;;contar o algarismos empilhdos
    inc CX      
 
    ;;repete se AX != 0   
    cmp AX, 0
    jnz LACO_DIGITO
  
LACO_ESCRITA:
    ;;desempilha unidade
    pop DX
    add DL, '0' ;adiciona '0' na parte baixa do DX
    mov AX, DX
    call ESCREVE_CHAR
	  dec CX ;;descrementa algarismo desempilhado
	  jnz LACO_ESCRITA
    ret
endp

inicio:
    mov AX, @DATA
    mov DS, AX
    
    ;chamada de procidure
    mov AX, 739
    call ESCREVE_INT16
            
    ;interrupcao de retorno
    mov AH, 4CH
    int 21H     
    
    

end inicio
