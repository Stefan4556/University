bits 32

global determina,afiseaza
extern printf
import printf msvcrt.dll  

segment data use32 class=data public

    cifra dd 0
    format db "%u",0
    lungime_maxima dd 0
    lungime_curenta dd 1    ; initializam cu 1 deoarece prima secventa e formata din cel putin 1 elem
 
segment code use32 class=code public
   
    determina:
        mov eax,[esp+4]
        mov ebx,0   ; in ebx o sa avem lungimea celei mai lungi secvente
        mov ecx,4
        determinare_prima_cifra:
            rcl eax,1
            rcl ebx,1
        loop determinare_prima_cifra
        mov ecx,7   ; avem 7 cifre hexa
        determinare_secventa:
            push ecx
            mov ecx,4
            mov edx,0 ; in edx salvam cifra curenta hexa
            determinare_cifra_hexa:
                rcl eax,1
                rcl edx,1
            loop determinare_cifra_hexa
            cmp ebx,edx ; facem compararea
            jb mergem_mai_departe
            jae nu_mergem_mai_departe
            mergem_mai_departe:
                inc dword[lungime_curenta]
                jmp pass
            nu_mergem_mai_departe:  ; in acest caz trebuie sa vedem cat este lungimea maxima
                pushad
                mov ebx,[lungime_curenta]
                cmp ebx,[lungime_maxima]
                jbe nu_actualizam
                    mov [lungime_maxima],ebx
                nu_actualizam:
                mov ebx,1
                mov [lungime_curenta],ebx
                popad
            pass:
            xchg ebx,edx    ; retinem cifra hexa precedenta
            pop ecx
        loop determinare_secventa
        ; facem o ultima verificare
        mov ebx,[lungime_curenta]
        cmp ebx,[lungime_maxima]
        jbe nu
            mov [lungime_maxima],ebx
        nu:
        mov ebx,[lungime_maxima]
    ret
    
    afiseaza:
        mov eax,[esp+4]
        mov ebx,0
        mov ecx,32
        biti:
            mov ebx,0
            rcl eax,1
            rcl ebx,1
            mov [cifra],ebx
            pushad

            push dword [cifra]
            push dword format
            call [printf]
            add esp,4*2

            popad
        loop biti
    ret