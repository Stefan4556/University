bits 32

global determinare_sir
; esp+4 - lungime
; esp+8 - sir_bytes_max
; esp+12 - sir
segment data use32 class = data public

    suma_bytes_max dw 0
    maxim_curent db 0

segment code use32 class = code public 

    determinare_sir:
    
    mov ecx,[esp+4]
    mov esi,[esp+12]
    mov edi,[esp+8]
    extragere:
        lodsb
        mov bl,0
        cmp al,bl
        jbe continua1
            mov bl,al
        continua1:
        lodsb 
        cmp al,bl
        jbe continua2
            mov bl,al
        continua2:
        lodsb 
        cmp al,bl
        jbe continua3
            mov bl,al
        continua3:
        lodsb 
        cmp al,bl
        jbe continua4
            mov bl,al
        continua4:
        mov al,bl
        stosb
        cbw
        add [suma_bytes_max],ax
        mov al,0
        mov bl,al
    loop extragere
    mov ax,[suma_bytes_max]
    cwde
    mov ebx,eax
    ret