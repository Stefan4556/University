bits 32        

global binar4
extern printf               
import printf msvcrt.dll    

; [esp] - adresa retur
; [esp + 4] - numar

segment data use32 class=data public
    contor dd 0
    format_afisare db "%d",0
    copie_eax dd 0
segment code use32 class=code public
    binar4:
        
        mov eax,[esp + 4]
        mov ecx,32
        repeta:
        
            mov [contor],ecx
            
            rcl eax,1
            
            mov [copie_eax],eax
            
            jc unu
            jnc zero
            
            unu:
                mov ebx,1
                jmp continua
            
            zero:
                mov ebx,0
            
            continua:
                push ebx
                push dword format_afisare
                call [printf]
                add esp,4*2
            
            mov ecx,[contor]
            mov eax,[copie_eax]
            
        loop repeta
    
    ret