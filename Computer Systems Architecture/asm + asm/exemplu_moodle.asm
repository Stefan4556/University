bits 32

global start        

extern exit,printf               
import exit msvcrt.dll
import printf msvcrt.dll    

segment data use32 class=data

    sir1 DD 1245AB36h, 23456789h, 1212F1EEh
    ls1 equ ($-sir1)/4
    sir2 times ls1 db 0
    ls2 dd 0
    cifra dd 0
    format db "%d",0
    space db " ",0
    sir3 times ls1*3 db 0

segment code use32 class=code
    start:

        mov esi,sir1
        mov edi,sir2
        mov ecx,ls1
        jecxz sfarsit1
        
        repeta:
        
            lodsd
            mov bl,ah
            cmp bl,0
            jge nu_retine
            
                mov al,bl
                stosb
                inc dword[ls2]
            
            nu_retine:
        
        loop repeta
        
        mov ecx,[ls2]
        jecxz sfarsit1
        mov esi,sir2
        repeta1:
            
            push ecx
            mov ecx,8
            lodsb
            mov dl,0
            conversie:
                
                push ecx
                mov dl,0
                mov bl,al
                clc
                rcl al,1
                rcl dl,1
                mov ebx,0
                mov bl,dl
                mov [cifra],ebx
                pushad
                push dword [cifra]
                push dword format
                call [printf]
                add esp,4*2
                popad
                pop ecx
                
                jmp pass
                    
                    sfarsit1:
                        jmp sfarsit
                    
                pass:
                
            loop conversie
            
            push dword space
            call [printf]
            add esp,4
            
            pop ecx
        
        loop repeta1
        
        mov esi,sir2
        mov ecx,[ls2]
        mov edi,sir3
        string:
            
            mov al,"-"
            stosb
            lodsb   ; punem in al byte ul din sir
            neg al
            mov bl,0
            impartiri:  ; de refacut bucata asta de cod
                cbw ; in ax o sa ajunga al
                div bl ; ah - rest al - cat
                mov bh,al
                mov al,ah
                stosb
        
        loop string
        
        
        
        sfarsit:
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
