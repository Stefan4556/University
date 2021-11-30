bits 32

global start        

extern exit,scanf,Numarare_litere_mari,afisare_continut_fisier             
import exit msvcrt.dll
import scanf msvcrt.dll                        

segment data use32 class=data

    format_citire db "%s",0
    nume_fisier times 20 db 0
    End_fisier db "end",0
    Nr_max_lit dd 0
    nume_fisier_max times 20 db 0

segment code use32 class=code
    start:
       
       
    Citeste_nume_fisier:
    
        ;scanf("%s",nume_fisier)
        
        push dword nume_fisier
        push dword format_citire
        call [scanf]
        add esp,4*2
        
        mov ecx,3
        mov esi,nume_fisier
        mov edi,End_fisier
        
        Compara:
            
            Cmp byte[esi],0
            je end_sir1
            cmpsb
            jz Compara
            jnz Procesare_fisier
            
            end_sir1:
            
            cmp byte[edi],0
            je afisare_rezultat_final
            
                Procesare_fisier:
                    
                    Push dword nume_fisier
                    call Numarare_litere_mari   ; in eax ajunge numarul de litere mari
                    add esp,4
                    Cmp eax,[Nr_max_lit]    ; verificam daca este depasit maximul
                    jb Citeste_nume_fisier
                    mov [Nr_max_lit],eax
                    mov esi, nume_fisier
                    mov edi, nume_fisier_max
                        Copiere:
                            movsb
                            cmp byte[esi],0
                            jne Copiere
                        mov byte[edi],0
                        
            jmp Citeste_nume_fisier
            
            afisare_rezultat_final:
                
                push dword nume_fisier_max
                call afisare_continut_fisier
                add esp,4*1
        
        push    dword 0
        call    [exit]
