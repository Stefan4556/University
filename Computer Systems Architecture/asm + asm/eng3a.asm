bits 32 

global start        

extern exit,scanf,printf,determinare_sir               
import exit msvcrt.dll  
import scanf msvcrt.dll
import printf msvcrt.dll  

segment data use32 class=data

    sir dd 1234A678h,12345678h,1AC3B47Dh,0FEDC9876h
    lungime equ ($-sir)/4
    sir_bytes_max times lungime db 0
    format_unsinged db "%u ",0
    format_suma db 10,"%d",0
    suma dd 0
    nr dd 0

segment code use32 class=code
    
    start:
        push dword sir
        push dword sir_bytes_max
        push dword lungime
        call determinare_sir
        add esp,4*3
        ; in ebx vine suma si sirul e construit deja
        mov esi,sir_bytes_max
        mov ecx,lungime
        afisare:
            mov eax,0
            lodsb
            mov [nr],eax
            push ecx
            push dword [nr]
            push dword format_unsinged
            call [printf]
            add esp,4*2
            pop ecx
        loop afisare
        mov [suma],ebx
        push dword [suma]
        push dword format_suma
        call [printf]
        add esp,4*2
        
     push    dword 0     
     call    [exit]       
