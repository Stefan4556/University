bits 32

global start        

extern exit,fopen,fclose,scanf,printf,fprintf               
import exit msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll     
import scanf msvcrt.dll   
import printf msvcrt.dll
import fprintf msvcrt.dll

segment data use32 class=data
    
    sir times 101 db 0
    format_string db "%s",0
    accesare_fisier db "w",0
    descriptor dd -1
    fisier times 101 db 0
    format_hexa db "%x",0
    cifra dd 0
    format_cifra db "%d ",0
    
segment code use32 class=code
    start:
    
    push dword sir
    push dword format_string
    call [scanf]
    add esp,4*2
    
    mov esi,sir
    mov bl,0
    repeta_citire:
    
          lodsb
          cmp al,bl
          
    jne repeta_citire
    
    mov edi,esi
    dec edi
    mov al,"."
    stosb
    mov al,"t"
    stosb
    mov al,"x"
    stosb
    mov al,"t"
    stosb
    mov al,0
    stosb
    
    push dword accesare_fisier
    push dword sir
    call [fopen]
    add esp,4*2
        
    cmp eax,-1
    je sfarsit
    
        mov [descriptor],eax
        
        push dword [descriptor]
        push dword format_hexa
        call [printf]
        add esp,4*2
        ; extragem cifrele 
        mov eax,[descriptor]
        extragem_cifre:
            
            mov edx,0
            mov ecx,10
            div ecx ; edx - rest , eax - cat
            mov ebx,eax     ; salvam in ebx cat-ul precedent
            mov ax, dx
            mov cl,2
            div cl          ; ah - rest, al - cat 
            cmp ah,0
            jne continua
            
                mov [cifra],edx
                pushad
                push dword [cifra]
                push dword format_cifra
                push dword [descriptor]
                call [fprintf]
                add esp,4*3
                popad
                
            continua:
         
            cmp ebx,0
        jne extragem_cifre
        
        push dword [descriptor]
        call [fclose]
        add esp,4
    
    sfarsit:
    
        push    dword 0      
        call    [exit]       
