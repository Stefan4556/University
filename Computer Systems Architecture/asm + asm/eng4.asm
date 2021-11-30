bits 32

global start

extern exit,printf
import exit msvcrt.dll
import printf msvcrt.dll

segment data use32 class = data

    sir dq 1110111b,100000000h,0ABCD0002E7FCh,5
    lsir equ ($-sir)/8
    rez times lsir dd 0
    curent_degree dd 0
    lungime_rez dd 0
    cifra dd 0
    format db "%d",0
    space db " ",0

segment code use32 class = code

    start:
    
    mov ecx,lsir
    mov esi,sir
    mov edi,rez
    jecxz sfarsit1
        
        parcurgere:
        mov eax,0
        mov bl,0    ; cu ajutorul lui bl determinam cati de 1 avem 
        mov [curent_degree],eax
            lodsd   ; incarcam dwordul inferior
            mov edx,eax
            push ecx
            mov ecx,32  ; numarul de biti al unui dword
            determinare_degree:
                rcl edx,1
                jc increase
                jnc verify
                increase:
                    inc bl
                    jmp pass
                verify:
                    cmp bl,3
                    jb pass1    ; inseamna ca secv noastra e mai mica decat 2
                        inc dword[curent_degree]
                    pass1:
                    mov bl,0
                pass:
            loop determinare_degree
            jmp eticheta
                sfarsit1:
                    jmp sfarsit
            eticheta:
            cmp bl,3
            jb pass2
                inc dword[curent_degree]
            pass2:
            mov ecx,[curent_degree]
            cmp ecx,2
            jb nu_retinem
                stosd
                inc dword [lungime_rez]
            nu_retinem:
            pop ecx
            add esi,4
        loop parcurgere
        
        mov esi,rez
        mov ecx,[lungime_rez]
        afisare:
            lodsd
            push ecx
            mov ecx,32
            baza2:
                rcl eax,1
                mov edx,0
                rcl edx,1
                mov [cifra],edx
                pushad
                push dword [cifra]
                push dword format
                call [printf]
                add esp,4*2
                popad
            loop baza2
            push dword space
            call [printf]
            add esp,4
            pop ecx
        loop afisare
        
    sfarsit: 
    push dword 0
    call [exit]