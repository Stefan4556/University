bits 32 

global start        

extern exit,scanf,printf               
import exit msvcrt.dll  
import scanf msvcrt.dll
import printf msvcrt.dll  

segment data use32 class=data

    n dd 0
    numar dd 0
    suma_curenta dd 0
    format db "%d",0
    sir times 10 dd 0   ; ar trb sa fie 65535
    sir_sume times 10 db 0  ; ar trb sa fie 65535
    cifra db 0

segment code use32 class=code
    start:
    push dword n
    push dword format
    call [scanf]
    add esp,4*2
    mov ecx,[n]
    mov edi,sir
    citeste:
        push ecx
        push dword numar
        push dword format
        call [scanf]
        add esp,4*2
        pop ecx
        mov eax,[numar]
        stosd
    loop citeste
    mov edi,sir_sume
    mov ecx,[n]
    mov esi,sir
    aflare_suma:
        mov eax,0
        mov [suma_curenta],eax
        lodsd
        suma:
            cdq ; eax <- edx : eax
            mov ebx,10
            div ebx ; edx - rest si eax cat
            xchg edx,eax    ; edx <-> eax
            mov [cifra],al
            mov bl,2
            div bl  ; ah - rest, al - cat 
            cmp ah,0
            jne continua
                mov eax,0
                mov al,[cifra]
                add [suma_curenta],eax
            continua:
            mov eax,edx ; mutam inapoi catul
            cmp eax,0
         jne suma   ; daca mai avem cifre inseamna ca mai trb sa mai calculam
            mov eax,[suma_curenta]
            stosb
    loop aflare_suma        
        push    dword 0     
        call    [exit]       
