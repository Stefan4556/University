bits 32
;Sa se scrie un program care citeste un fisier text care contine propozitii (propozitiile sunt separate 
;de caracterul '?') si scrie intr-un alt fisier doar propozitiile de ordin de forma 3k+1 (i.e. scrie 
;propozitia 1, 4, 7, ...). Numele celor 2 fisiere se dau in segmentul de date.
global start        

extern exit,fopen,fclose,fscanf,fprintf               
import exit msvcrt.dll           
import fopen msvcrt.dll
import fclose msvcrt.dll
import fscanf msvcrt.dll
import fprintf msvcrt.dll

segment data use32 class=data

    fisier1 db "fisier1-3k.txt",0
    fisier2 db "fisier2-3k.txt",0
    acces1 db "r",0
    acces2 db "w",0
    format_caracter db "%c",0
    caracter dd 0
    descriptor1 dd 0
    descriptor2 dd 0
    indice dw 0
    rest_imp dw 0

segment code use32 class=code
    start:

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
        mov bx,[indice] 
        citeste:
            
                push dword caracter
                push dword format_caracter
                push dword [descriptor1]
                call [fscanf]
                add esp,4*3
                
                cmp eax,-1
                je afara
                    
                mov dx,[rest_imp]
                cmp dx,1
                jne nu_afiseaza
                    
                    push dword [caracter]
                    push dword format_caracter
                    push dword [descriptor2]
                    call [fprintf]
                    add esp,4*3
                    
                nu_afiseaza:
                
                mov ecx,[caracter]
                cmp ecx,"?"
                jne continua
                    
                    inc bx
                    mov ax,bx
                    mov dx,0
                    mov cx,3
                    div cx
                    mov [rest_imp],dx
                
                continua:
                
        jmp citeste
        
        afara:
            
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
