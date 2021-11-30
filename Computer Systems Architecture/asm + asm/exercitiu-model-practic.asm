bits 32

global start        

extern exit,printf               
import exit msvcrt.dll
import printf msvcrt.dll    

segment data use32 class=data
   
    sir dd 125,215,-125
    lungime_sir equ ($ - sir) / 4
    sir_word times lungime_sir*2 dw 0
    cifra db 5
    numar_maxim dw 0
    numar_minim dw 0
    format_afisare db "%s ",0
    contor dd 0
    copie_word dw 0
    copie_word_2 dw 0

segment code use32 class=code
    start:
        
    mov esi,sir ; punem in esi sirul de dword-uri
    mov edi,sir_word
    mov ecx,lungime_sir
    mov bx,10 
    jecxz sfarsit
    repeta:
    
            lodsd
            cmp eax,0   ; verificam daca numarul este pozitiv
            jl continua
            
            mov [copie_word_2],ax   ; eax = w1 w2 ; in dx = w2
            ror eax,16  ; ax = w1
            mov [copie_word],ax
            cwd
            idiv bx ; dx - rest, ax - cat
            cmp dx,[cifra]
            jne continua1    ; daca e egal stocam wordul
            
            mov ax,[copie_word]
            stosw
            
            continua1:  ; verificam urmatorul word\
            
            mov ax,[copie_word_2]
            cwd
            idiv bx
            
            cmp dx,[cifra]
            jne continua
            
            mov ax,[copie_word_2]
            stosw            
            
            continua:
    
    loop repeta
    
    push dword [sir_word]
    push dword format_afisare
    call [printf]
    add esp,4*2
    
    sfarsit:
        push    dword 0     
        call    [exit]       
