bits 32 

global start       

extern exit,determinare_secventa_impara,printf      
import exit msvcrt.dll
import printf msvcrt.dll
  
segment data use32 class=data public

    s db 12,13,10b,7,-3,100,101b,11h,27,-1,4
    ls1 equ $-s
    sir_maxim times ls1 db 0
    lsmaxim dd 0
    format_afisare_hexa db "%xh, ",0
    numar dd 0
    ls1_var dd 0

segment code use32 class=code public
    start:
        
        mov dword[ls1_var],ls1
        push dword [ls1_var]
        push dword s
        push dword sir_maxim
        push dword [lsmaxim]
        call determinare_secventa_impara
        add esp,4*4
        ; dupa acest apel avem in sir_maxim sirul si in lsmaxim lungimea acestuia
        
        mov esi,sir_maxim
        ;mov ecx,[lsmaxim]
        afisare:
            mov eax,0
            lodsb
            mov [numar],eax
            push ecx
          
            push dword [numar]
            push dword format_afisare_hexa
            call [printf]
            add esp,4*2
            
            pop ecx
        
        loop afisare
        
        push dword 0      
        call [exit]       
