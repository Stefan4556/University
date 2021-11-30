bits 32 ; assembling for the 32 bits architecture       

global hexa4
extern printf               
import printf msvcrt.dll   

; ESP - adresa retur 
; ESP + 4 - adresa sir
; ESP + 8 - lungimea sir

segment data use32 class=data public
    format_afisare db "%x ",0
    contor dd 0
    
segment code use32 class=code public

    hexa4:
        mov ecx,[ESP+8]
        
        mov esi,[ESP+4]
        
        repeta:
            
            mov eax,0
            lodsd
            mov [contor],ecx
            push eax
            push dword format_afisare
            call [printf]
            add esp,4*2
            
            mov ecx,[contor]
            
        loop repeta
    
    ret
    
       
