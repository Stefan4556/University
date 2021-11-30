bits 32  
global _Transformare                       
segment data public data use32
   ;numar resw 1
   sir2 resb 8
   
segment code public code use32

mov edi,[sir2]

_Transformare:	
    mov edi,[sir2]
    push ebp
	mov ebp, esp	
    lea esi,[ebp+8]    
	;mov eax, [ebp+8]
    ;mov word [numar],ax   
    ;mov esi,numar
	mov bl,0
    mov ecx,0
	.repet: 
		  lodsb;al=primul caracter
          cmp al,'b'
          je .oprire
          sbb al,'0'
          jnc .shiftare_cu_1
          jc .shiftare_cu_0
          
          .shiftare_cu_1:
                  stc
                  jmp .continua
          .shiftare_cu_0:
                  clc
                  
          .continua: rcl bl,1
              
	loop .repet
    .oprire: mov al,bl
            stosb    
    
    mov esp, ebp
	pop ebp
	ret 
