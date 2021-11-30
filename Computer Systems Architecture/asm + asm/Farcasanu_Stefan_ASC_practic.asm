bits 32 
global start        

extern exit, printf, scanf, gets, fopen, fclose, fprintf, fread, fscanf             
import exit msvcrt.dll              
import printf msvcrt.dll              
import scanf msvcrt.dll              
import gets msvcrt.dll              
import fopen msvcrt.dll              
import fclose msvcrt.dll              
import fprintf msvcrt.dll              
import fread msvcrt.dll              
import fscanf msvcrt.dll 
   
segment data use32 class=data
    nume_fisier times 30 db 0
    caracter dd 0
    formats db "%s", 0
    formatc db " %c", 0
    format_scriere db "%s ", 0
    mod_accesr db "r", 0
    mod_accesw db "w", 0
    mod_accesa db "a", 0
    descriptor dd -1
    output db "output.txt", 0
    descriptor_output dd - 1
    len equ 100
    buffer times 100 db 0
    cuvant times 30 db 0
    
segment code use32 class=code
    start:
        
        ; deschidem fisierul de output, daca nu exista il creeam
        push mod_accesw
        push output
        call [fopen]
        add esp, 4*3
        
        cmp eax, 0
        je final
        
        push eax
        call [fclose]   ; il si inchidem deoarece acesta fost creat
        
        push nume_fisier
        push formats
        call [scanf]
        add esp, 4*2    ; citim numele fisierului
        
        push caracter
        push formatc
        call [scanf]    ; citim caracterul
        add esp, 4*2
        
        push mod_accesr
        push nume_fisier
        call [fopen]    ; deschidem fisierul pe care l am citit din consola
        add esp, 4*2
        cmp eax, 0
        
        je final
        
        mov [descriptor], eax   ; mutam descriptorul fisierului de unde luam cuvintele
        
        push mod_accesa
        push output
        call [fopen]
        add esp, 4*2
        cmp eax, 0
        je final    ; deschidem fisierul unde o sa afisam
        
        mov [descriptor_output], eax    ; mutam descriptor
        
        citire:
            push dword[descriptor]
            push len
            push 1
            push buffer
            call [fread]
            add esp, 4*4    ; citim cu fread mai multe caractere
            
            cmp eax, 0
            je gata_cititul     ; daca nu mai sunt caractere am terminat
                
            mov ecx, eax    ; cate caractere avem in sir
            mov esi, buffer ; adresa unde e sirul
            mov edi, cuvant ; adresa unde o sa construim cuvantul
            
            parcurgere: ; parcurgem sirul curent
                lodsb   ; incarcam caracter cu caracter
                
                push ecx    ; dam push la ecx pt ca daca suntem la finalul unui cuvant o sa fie nevoie sa folosim frpintf, fct ce afecteaza registrii
                cmp al, " " ; daca e egal inseamna ca am ajuns la final de cuvant
                je cuvant_gata
                
                stosb
                jmp gata    ; gata ne duce inainte de loop insemnand ca inca mai are litere cuvantul curent
                
                cuvant_gata:    ; aici realizam verificarea legata de al doilea caracter
                mov al, 0
                stosb
                mov bl, [caracter]
                cmp [cuvant+1], bl
                jne out ; iesim daca nu e bun
                ; afisam cuvantul daca e bun
                push cuvant
                push format_scriere
                push dword[descriptor_output]
                call [fprintf]
                add esp, 4*3
                
                out:
                mov edi, cuvant ; reinitializam cuvantul
                
                gata:
                pop ecx ; punem val inapoi
            loop parcurgere ; mai jos se ajunge daca ultimul caracter din sirul curent nu este spatiu dar noi totusi avem un cuvant candidat
            ;verificam daca al doilea carac e ceea ce cautam
            mov al, 0
            stosb
            mov bl, [caracter]
            cmp [cuvant + 1], bl
            jne inchidere
            ; daca e ok il afisam
            push cuvant
            push format_scriere
            push dword[descriptor_output]
            call [fprintf]
            add esp, 4*3
            inchidere:
        jmp citire
        
        gata_cititul:
       ; inchidem fisierul din care luam date
        push dword[descriptor]
        call [fclose]
        add esp, 4
        ; inchidem fisierul in care afisam
        push dword[descriptor_output]
        call [fclose]
        add esp, 4
        
        final:
        
        push    dword 0      
        call    [exit]       
