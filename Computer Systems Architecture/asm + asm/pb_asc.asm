bits 32 

global start        

extern exit, scanf, gets, printf, fopen, fclose, fread, fscanf, fprintf  
import exit msvcrt.dll  
import scanf msvcrt.dll
import gets msvcrt.dll
import printf msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll
import fread msvcrt.dll
import fscanf msvcrt.dll
import fprintf msvcrt.dll   

segment data use32 class=data
    ; ...
    fisier1 times 20 db 0
    fisier2 db "output.txt", 0
    modacces1 db "r", 0
    modacces2 db "a", 0
    descriptor1 dd -1
    descriptor2 dd -1
    
    format db "%s", 0
    formatc db " %c", 0
    formats db "%s ", 0
    c dd 0
    buffer times 100 db 0
    cuvant times 20 db 0

segment code use32 class=code
    start:
        ; ne ocupam cu citirea primului fisier
        push dword fisier1
        push dword format
        call [scanf]
        add esp, 4*2
        
        ; ne ocupam cu citirea caracterului c
        push dword c
        push dword formatc
        call [scanf]
        add esp, 4*2
        
        ; ne ocupam cu deschiderea fisierului din care citim cuvintele
        push dword modacces1
        push dword fisier1
        call [fopen]
        add esp, 4*2
        
        cmp eax, 0
        je final
        
        mov [descriptor1], eax  ; mutam in descriptor adresa fisierului de unde citim
        
        ; deschidem si al doilea fisier
        push dword modacces2
        push dword fisier2
        call [fopen]
        add esp, 4*2
        
        cmp eax, 0
        je final
        
        mov [descriptor2], eax  ; mutam in cel de al doilea descriptor adresa fisierului in care o sa scriem
        
        ; incepem sa citim din fisier
        bucla:
            push dword[descriptor1]
            push dword 100
            push dword 1
            push buffer
            call [fread]
            add esp, 4*4

            
            cmp eax, 0  ; daca nu se mai poate citi o sa iesim
            je out
            
            mov ecx, eax
            mov esi, buffer ; adresa unde este salvat sirul citit
            mov edi, cuvant ; adresa unde formam cuvantul rezultat
            parcurgere: ; ne apucam sa parcurgem ceea ce am citit din fisier cu fread
                lodsb 
                cmp al, " " ; daca suntem pe un caracter spatiu inseamna ca am ajuns la finalul unui cuvant
                je next
                stosb      ; daca nu aici o sa retinem cuvantul in cuvant
                jmp out2
                next:   ; daca am ajuns aici inseamna ca am terminat de retinut un cuvant
                    mov al, 0   
                    stosb   ; punem 0 la final pentru a l face string
                    mov al, byte[c]
                    cmp byte[cuvant+1], al  ; vedem daca a doua litera este egala cu ltiera pe care noi am citit o din consola
                    jne out3    ; daca caracterul nu e egal inseamna ca nu trb sa l afisam
                    pushad  ; punem registrii pe stiva deoarece urmeaza sa apelam o functie din c
                    push cuvant
                    push formats
                    push dword[descriptor2]
                    call [fprintf]
                    add esp, 4*3 
                    popad   ; punem registrii inapoi pentru ca am terminat de apelat
                out3:
                mov edi, cuvant
                out2:
            loop parcurgere
            
            mov al, 0   
            stosb
            mov al, byte[c]
            cmp byte[cuvant+1], al  ; aici daca a 
            jne out3
            pushad
            push cuvant
            push formats
            push dword[descriptor2]
            call [fprintf]
            add esp, 4*3 
            popad
            
            jmp bucla
        out:
        
        ; inchidem primul fisier 
        push dword[descriptor1]
        call [fclose]
        add esp, 4
        
        ; inchidem cel de al doilea fisier
        push dword[descriptor2]
        call [fclose]
        add esp, 4
        
        final:

        push    dword 0     
        call    [exit]       
