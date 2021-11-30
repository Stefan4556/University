bits 32

global start        

extern exit,scanf,fopen,fscanf,fclose,printf               
import exit msvcrt.dll
import scanf msvcrt.dll
import fopen msvcrt.dll
import fscanf msvcrt.dll            
import fclose msvcrt.dll           
import printf msvcrt.dll

segment data use32 class=data

    format_citire db "%d",0
    format_citire_fisier db "%s",0
    fisier_citire times 21 db 0
    numar dd 0
    descriptor dd -1
    format_deschidere_fisier db "r",0
    format_citire_2 db "%c",0
    caracter dd 0
    diferenta dd 0
    format_afisare db "%d",0

segment code use32 class=code
    start:
    ; ne ocupam cu citirea numelui fisierului
    push dword fisier_citire
    push dword format_citire_fisier
    call [scanf]
    add esp,4*2
    
    ; ne ocupam cu citirea numarului
    push dword numar
    push dword format_citire
    call [scanf]
    add esp,4*2
    
    ; deschidem fisierul
    push dword format_deschidere_fisier
    push dword fisier_citire
    call [fopen]
    add esp,4*2
    
    cmp eax,0
    je sfarsit  ; daca descriptorul e 0 inseamna ca a intampinat o eroare
        
        mov [descriptor],eax
        
        repeta:
        
            ; citim cate un caracter desc,form,adr
            mov eax,0
            push dword caracter
            push dword format_citire_2
            push dword [descriptor]
            call [fscanf]
            add esp,4*3
            
            ; conditia de oprire
            cmp eax,-1
            je continua
            
            mov eax,[caracter]  ; in al se afla de fapt caracterul nostru
            ; extragem bitul de care avem nevoie
            
            mov ecx,[numar] ; vedem de ce bit avem nevoie
            add ecx,1   ; adaugam 1 deoarece noi incercam sa retinem bitul cu ajutorul carry flag
            extrage:
                
                rcr eax,1
                
            loop extrage
            mov ebx,0
            rcl ebx,1   ; punem in bl bit-ul pe care l am extras
            sub [diferenta],ebx
         
         jmp repeta
         continua:
         ; ne ocupam cu afisarea diferentei
         push dword [diferenta]
         push dword format_afisare
         call [printf]
         add esp,4*2
         
         ; inchidem fisierul
         push dword [descriptor]
         call [fclose]
         add esp,4
        
    sfarsit:
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
