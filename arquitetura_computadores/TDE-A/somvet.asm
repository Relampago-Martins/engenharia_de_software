.model small
.stack 100H  
.data 
    TAM_VETOR EQU 5             	; define uma constante de valor 5
    vetor dw 1, 2, 3, 4, 5      		; define um vetor de 5 posi��es
.code 

SOMA_VETOR16 proc
    push BX   
    push CX 
    
    ; Soma os valores do vetor
    xor AX, AX                 	
    mov BX, offset vetor         		; BX recebe a posi��o inicial do vetor
    mov CX, TAM_VETOR           	; CX = n�mero de elementos do vetor

 ACUMULA:          
    add AX,[BX]			;BX cont�m o valor da primeira posi��o  
    add BX, 2 				;pula 2 posi��es pois numero tem 2 bytes
    loop ACUMULA 			;decrementa de CX=5 at� CX=0         
                     	
    pop CX    
    pop BX    
ret
endp    

PRINT16 proc
    ; Exibe o resultado na tela
    push AX                    
    push CX
    push DX 
    
    xor DX, DX                   		; Zera DX para divis�o
    mov BX, 10                   		; Divisor para separa��o de d�gitos
    xor CX, CX                   		; Zera o contador de d�gitos

    LACO_DIV:
    xor DX, DX   			;zerar DX pois o dividendo � DXAX
    div BX       				;divis�o para separar o d�gito em DX
    push DX     
    inc CX       				;incrementa o contador para chegar at� CX=5
    cmp AX, 0    		
    jnz LACO_DIV 			;enquanto AX =! 0 salte para LACO_DIV
           
    LACO_ESCDIG:
    pop DX       				;desempilha o d�gito    
    add DL, '0'  				;converter o d�gito para ASCII
    call ESC_CHAR               
    loop LACO_ESCDIG    		;decrementa CX=5 at� CX=0
          
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

    call SOMA_VETOR16  
    ; Multiplica o resultado por 2
    shl AX, 1 ; Chama a rotina para somar, multiplicar e exibir o resultado
    call PRINT16        
      
    mov ah, 4ch
    int 21h
end INICIO