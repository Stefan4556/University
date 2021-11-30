bits 32

global Numarare_litere_mari

extern fopen,fclose,fscanf
import fopen msvcrt.dll
import fclose msvcrt.dll
import fscanf msvcrt.dll

segment data use32 class = data public

    mod_acces db "r",0
    Format db "c",0
    descriptor dd -1
    caracter times 2 db 0
    contor dd 0

segment code use32 class = code public

Numarare_litere_mari:
    
    mov eax,[esp+4]
    
    push dword mod_acces
    push eax
    call [fopen]; eax - descriptor sau 0
    add esp,4*2
    
    mov [descriptor],eax
    cmp eax,0
    jz sfarsit_1
    
        mov dword[contor],0
    
        Citire:
            
            Push dword caracter
            push dword Format
            push dword [descriptor]
            call [fscanf] ; la adresa caracter vom aveam caracterul actual citit
            add esp,4*3
            
            Cmp byte [caracter],0
            je sfarsit_2
            
            Cmp byte [caracter],'A'
            jb Nu_este_litera_mare
            
            cmp byte [caracter],'Z'
            ja Nu_este_litera_mare
            
            inc dword [contor]
            
            Nu_este_litera_mare:
                jmp Citire
    
    sfarsit_2:
    
        push dword [descriptor]
        call [fclose]
        add esp,4
    
    sfarsit_1:
    
        mov eax,[contor]
    
    ret
    
