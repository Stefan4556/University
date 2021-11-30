bits 32

global start        

extern exit,printf               
import exit msvcrt.dll
import printf msvcrt.dll    

segment data use32 class=data

    sir db 1,2,3,4,5
    len equ $ - sir
    format_afisare db "%d ",0
    rand_liber db 10,0
    contor dd 0

segment code use32 class=code
    start:
    mov ecx,len
    ; prima data afisam de la stanga la dreapta elementele
    cld
    mov esi,sir
    repeta:
        
        mov eax,0
        lodsb
        mov [contor],ecx
        push eax
        push dword format_afisare
        call [printf]
        add esp,4*2
        mov ecx,[contor]
        
    loop repeta
    
    push dword rand_liber
    call [printf]
    add esp,4*1
    
    mov ecx,len
    ; afisam de la dreapta la stanga
    mov esi,sir
    add esi,len
    sub esi,1   ; punem in esi sir + len - 1
    std
    repeta1:
    
        mov [contor],ecx
        mov eax,0
        lodsb
        push eax
        push dword format_afisare
        call [printf]
        add esp,4*2
        mov ecx,[contor]
    
    loop repeta1
    
        push    dword 0      
        call    [exit]    
