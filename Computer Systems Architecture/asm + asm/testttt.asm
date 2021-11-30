bits 32 

global start        

extern exit,determina,afiseaza,printf               
import exit msvcrt.dll   
import printf msvcrt.dll 

segment data use32 class=data

    d dd 2, -1, 0ABCh, 0FFEh, 0ABCF2h, 1235FFh, -2, 12235ABFh
    lung_d equ ($-d)/4
    virgula_spatiu db ", ",0

segment code use32 class=code
    start:
    
    mov esi,d
    mov ecx,lung_d
    parcurege_sir:
    
        lodsd
        push ecx
        push eax
        push eax
        call determina
        add esp,4*1
        ; o sa returnam in ebx daca lungimea e minim 5
        
        pop eax
        cmp ebx,5
        jb nu_afisam
            push dword eax
            call afiseaza
            add esp,4
            
            push dword virgula_spatiu
            call [printf]
            add esp,4
        nu_afisam:
        pop ecx
    loop parcurege_sir
    
        push    dword 0      
        call    [exit]       
