bits 32

global afisare_continut_fisier

extern printf,fopen,fread,fclose
import printf msvcrt.dll
import fopen msvcrt.dll
import fread msvcrt.dll
import fclose msvcrt.dll

segment data use32 class = data public

    mod_acces db "r",0
    descriptor dd -1
    Newline db 10,13,0
    rez times 101 db 0

segment code use32 class = data public

    afisare_continut_fisier:
    ; afisare_continut_fisier(nume_fisier)
    ; ESP + 4 - nume_fisier
    
    ; printf(*nume_fisier)
    mov eax,[esp+4] ; eax - adresa nume fisier
    
    push eax
    call [printf]
    add esp,4*1
    
    push dword Newline
    call [printf]
    add esp,4*1
    
    ;fopen(nume_fisier,"r")
    mov eax,[esp+4]
    push dword mod_acces
    push eax
    call [fopen]
    add esp,4*2 ; in eax avem descriptor sau 0 daca e eroare
    
    mov [descriptor],eax
    cmp eax,0
    je sfarsit_2
    repeta:
    
        ;fread(*rez,1,100,descriptor)
        push dword [descriptor]
        push dword 100
        push dword 1
        push dword rez
        call [fread]
        add esp,4*4 ; eax contine numarul de elemente citite
        
        cmp eax,0
        je sfarsit_1  ; daca nu e 0 avem elemente
        
        ;printf(*rez)
        mov byte[rez+eax],0
        push dword rez
        call [printf]
        add esp,4*1
    
    jmp repeta
    
    sfarsit_1:
    
    ;fclose(descriptor)
    push dword [descriptor]
    call [fclose]
    add esp,4*1
    
    sfarsit_2:
    
    Ret