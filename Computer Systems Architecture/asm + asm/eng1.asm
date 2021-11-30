bits 32

global start        

extern exit,printf               
import exit msvcrt.dll
import printf msvcrt.dll    

segment data use32 class=data

    sir dd 1234A678h,12785634h,1A4D3C26h
    lsir equ ($-sir)/4
    sir_worduri times lsir dw 0
    suma_biti dd 0
    format db "%d",0

segment code use32 class=code
    start:
    mov ecx,lsir
    mov esi,sir
    mov edi,sir_worduri
    jecxz sfarsit
    repeta:
        mov ebx,0
        lodsb
        lodsb
        mov bl,al
        lodsb
        lodsb
        mov bh,al   ; in bx se formeaza wordul
        mov ax,bx
        stosw
    loop repeta
    mov esi,sir_worduri
    mov ecx,lsir
    parcurgere:
        lodsw
        push ecx
        mov ecx,16
        ;clc
        extragere:
            rcl ax,1
            jnc continua
                inc dword [suma_biti]
            continua:
        loop extragere
        pop ecx
    loop parcurgere
    push dword [suma_biti]
    push dword format
    call [printf]
    add esp,4*2
    sfarsit:
        push    dword 0      
        call    [exit]      
