bits 32

global start        

extern exit,fopen,fclose,fscanf,fprintf               
import exit msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll
import fscanf msvcrt.dll
import fprintf msvcrt.dll    

segment data use32 class=data

    fisier1 db "fisier1.txt",0
    fisier2 db "fisier2.txt",0
    acces1 db "r",0
    acces2 db "w",0
    descriptor1 dd 0
    descriptor2 dd 0
    contor_paritate dd 0
    caracter dd 0
    format db "%c",0

segment code use32 class=code
    start:

        ;fopen(fis,mod) - pentru a deschide cele 2 fisiere
        
        push dword acces1
        push dword fisier1
        call [fopen]
        add esp,4*2
        
        cmp eax,0
        je sfarsit
        
        mov [descriptor1],eax
        
        push dword acces2
        push dword fisier2
        call [fopen]
        add esp,4*2
        
        cmp eax,0
        je sfarsit1
        
        mov [descriptor2],eax
        
        citeste:
            
            mov eax,0
            push dword caracter
            push dword format
            push dword [descriptor1]
            call [fscanf]
            add esp,4*3
            
            cmp eax,-1  ; conditia de oprire
            je continua
            
            mov eax,[caracter]
            mov ebx,[contor_paritate]
            
            cmp ebx,0
            je par
            ; daca indicele e impar afisam caracterul
                push dword [caracter]
                push dword format
                push dword [descriptor2]
                call [fprintf]
                add esp,4*3
            par:
                mov eax,[caracter]
                cmp eax,"!"
                jne mai_departe ; daca nu e egal cu ! mergem mai departe
                    cmp ebx,0   ; vedem daca e par sau impar
                        je schimba_impar
                        jne schimba_par
                        schimba_impar:
                            mov ebx,1
                            mov [contor_paritate],ebx
                            jmp mai_departe
                        schimba_par:
                            mov ebx,0
                            mov [contor_paritate],ebx
             
                mai_departe:
            
        jmp citeste
        continua:
            
            push dword [descriptor2]
            call [fclose]
            add esp,4
            
        sfarsit1:
        
            push dword [descriptor1]
            call [fclose]
            add esp,4
        
        sfarsit:

        push    dword 0    
        call    [exit]     
