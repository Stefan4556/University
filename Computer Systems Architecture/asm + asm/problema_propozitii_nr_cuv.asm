bits 32
; Se afiseaza in fisier primul cuvant din fiecare propozitie urmat de numarul de cuvinte din aceasta
; Fiecare propozitie se termina cu caracterul ?

global start        

extern exit,fscanf,fprintf,fopen,fclose              
import exit msvcrt.dll
import fscanf msvcrt.dll
import fprintf msvcrt.dll   
import fopen msvcrt.dll
import fclose msvcrt.dll 

segment data use32 class=data
    
    fisier1 db "input-eng.txt",0
    acces1 db "r",0
    descriptor1 dd -1
    fisier2 db "output-eng.txt",0
    acces2 db "w",0
    descriptor2 dd -1
    format_caracter db "%c",0
    contor dd 0
    caracter dd 0
    format_numar db " %d ",0
    
segment code use32 class=code
    start:
        
       push dword acces1
       push dword fisier1
       call [fopen]
       add esp,4*2
       
       cmp eax,0
       je sfarsit1
       mov [descriptor1],eax
       
       push dword acces2
       push dword fisier2
       call [fopen]
       add esp,4*2
       
       cmp eax,0
       je sfarsit2
       mov [descriptor2],eax
       
       rezolva:
            
            mov ebx,[contor]    ; initializam contorul in ebx
            
            push dword caracter
            push dword format_caracter
            push dword [descriptor1]
            call [fscanf]
            add esp,4*3
            
            cmp eax,-1
            je afara
            
            mov eax,[caracter]
            cmp eax,"?"
            je afisam_rezultate
                
                mov eax,ebx
                cmp eax,0
                jne nu_afisam_primul_cuvant
                    mov eax,[caracter]
                    cmp eax," "
                    je nu_afisam_primul_cuvant
                
                    push dword[caracter]
                    push dword format_caracter
                    push dword [descriptor2]
                    call [fprintf]
                    add esp,4*3
                
                nu_afisam_primul_cuvant:
                    mov eax,[caracter]
                    cmp eax," "
                    jne continua
                        inc ebx
                        mov [contor],ebx
                        jmp continua
            
            afisam_rezultate:
                
                inc ebx
                
                push dword ebx
                push dword format_numar
                push dword [descriptor2]
                call [fprintf]
                add esp,4*3
                
                mov ebx,0
                mov [contor],ebx
            
            continua:
            
       jmp rezolva
       
       afara:
            
            push dword [descriptor2]
            call [fclose]
            add esp,4
            
       sfarsit2:
        
            push dword [descriptor1]
            call [fclose]
            add esp,4
       
       sfarsit1:
        
        push    dword 0      
        call    [exit]       
