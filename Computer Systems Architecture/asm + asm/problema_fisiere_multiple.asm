bits 32 

global start        

extern exit,fopen,fclose,fscanf,fprintf               
import exit msvcrt.dll   
import fopen msvcrt.dll
import fclose msvcrt.dll
import fscanf msvcrt.dll
import fprintf msvcrt.dll
                          
segment data use32 class=data

    nume_fisier db "fisier_multiplu.txt",0
    nume_fisier_universal db "output-c.txt",0
    accesare_fisier db "w",0
    accesare_fisier_citire db "r",0
    format_afisare_fisier db "%c",0
    format_citire_fisier db "%d",0
    descriptor dd -1
    sir db "abcdefgh",0
    numar dd 0
    copie_ecx dd 0
    copie_ecx_afiseaza dd 0

segment code use32 class=code
    start:
    
        ; citim numarul din fisier
        push dword accesare_fisier_citire
        push dword nume_fisier
        call [fopen]
        add esp,4*2
        
        cmp eax,0
        je sfarsit
        
        mov [descriptor],eax
        ; citim numarul din fisier
        push dword numar
        push dword format_citire_fisier
        push dword [descriptor]
        call [fscanf]
        add esp,4*3
        
        push dword [descriptor]
        call [fclose]
        add esp,4
        
        mov ecx,0
        
            creeaza:
            
                add cl,"0"
                mov [nume_fisier_universal+7],cl ; punem in loc de caracterul c cifra
                sub cl,"0"
                mov [copie_ecx],ecx
                
                ; cream fisierul
                push dword accesare_fisier
                push dword nume_fisier_universal
                call [fopen]
                add esp,4*2
                
                mov [descriptor],eax
                mov esi,sir ; ne ocupam cu afisarea primelor i+1 caractere
                mov ecx,[copie_ecx]
                add ecx,1
                
                    afiseaza:
                        
                        mov [copie_ecx_afiseaza],ecx
                        mov eax,0
                        lodsb
                        
                        push eax
                        push dword format_afisare_fisier
                        push dword [descriptor]
                        call [fprintf]
                        add esp,4*3
                        
                        mov ecx,[copie_ecx_afiseaza]
                    
                    loop afiseaza
                    
                    push dword [descriptor] ; inchidem fisierul curent
                    call [fclose]
                    add esp,4
                
                mov ecx,[copie_ecx]
                inc ecx
                cmp ecx,[numar]
                
        jbe creeaza
                
        sfarsit:
        
        push    dword 0      
        call    [exit]     
