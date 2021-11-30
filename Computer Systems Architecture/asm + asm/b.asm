bits 32

global determinare_secventa_impara        

segment dat use32 class=data public

    lungime_curenta dd 0
    lungime_maxima dd 0
    poz_inceput dd 0
    copie dd 0

segment cod use32 class=code public

    determinare_secventa_impara:
       
    mov ecx,[esp+16]
    mov esi,[esp+12]
    parcurgere:
        
        lodsb
        mov ah,0
        mov bl,2
        div bl ; ah - rest, al - cat
        cmp ah,0
        je sfarsit_secventa
            inc dword[lungime_curenta]
            jmp pass
        sfarsit_secventa:
            mov ebx,[lungime_curenta]
            cmp ebx,[lungime_maxima]
            jb nu_retinem
                mov [lungime_maxima],ebx    ; actualizam lungimea maxima
                mov ebx,esi
                sub ebx,[lungime_maxima]    ; ajungem la poz s-lung
                sub ebx,[esp+12]                   ; scadem s pentru a ajunge la poz unde incepe
                mov [poz_inceput],ebx
                mov ebx,0
                mov [lungime_curenta],ebx
            nu_retinem:
        pass:
     loop parcurgere
     ; ar trb sa avem pozitia de inceput si poz maxima
     mov ecx,[lungime_maxima]
     ;sub ecx,[poz_inceput]  ; avem lungimea sirului
     mov [esp+4],ecx
     mov [copie],ecx
     mov esi,[esp+12]
     add esi,[poz_inceput]
     sub esi,1
     mov edi,[esp+8]
     muta:
        movsb
     loop muta
     mov ecx,[copie]
     ret