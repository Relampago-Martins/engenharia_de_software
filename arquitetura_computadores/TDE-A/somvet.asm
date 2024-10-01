.model small
.stack 100H  
.data 
    TAM_VETOR EQU 5             	; define uma constante de valor 5
    vetor dw 1, 2, 3, 4, 5      		; define um vetor de 5 posições
.code 

SOMA_VETOR16 proc
    xor AX, AX    
 ACUMULA:          
    add AX,[BX]			;BX contém o valor da primeira posição  
    add BX, 2 				;pula 2 posições pois numero tem 2 bytes
    loop ACUMULA 			;decrementa de CX=5 até CX=0         
ret
endp    

PRINT16 proc
    ; Exibe o resultado na tela
    push AX                    
    push CX
    push DX 
    
    xor DX, DX                   		; Zera DX para divisão
    mov BX, 10                   		; Divisor para separação de dígitos
    xor CX, CX                   		; Zera o contador de dígitos

    LACO_DIV:
    xor DX, DX   			;zerar DX pois o dividendo é DXAX
    div BX       				;divisão para separar o dígito em DX
    push DX     
    inc CX       				;incrementa o contador para chegar até CX=5
    cmp AX, 0    		
    jnz LACO_DIV 			;enquanto AX =! 0 salte para LACO_DIV
           
    LACO_ESCDIG:
    pop DX       				;desempilha o dígito    
    add DL, '0'  				;converter o dígito para ASCII
    call ESC_CHAR               
    loop LACO_ESCDIG    		;decrementa CX=5 até CX=0
          
    pop DX  
    pop CX    
    pop AX
    ret
endp

ESC_CHAR proc
    push AX ;empilha reg para salvar valor
    mov AH, 2
    int 21H   
    pop AX ;desempilha reg
    ret
endp 

  
  
INICIO:  
    mov AX, @DATA
    mov DS, AX 

    ;define parametros
    mov BX, offset vetor            ; BX recebe a posição inicial do vetor
    mov CX, TAM_VETOR           	; CX = número de elementos do vetor
    call SOMA_VETOR16  
    ; Multiplica o resultado por 2
    shl AX, 1 ; Chama a rotina para somar, multiplicar e exibir o resultado
    call PRINT16        
      
    mov ah, 4ch
    int 21h
end INICIO
