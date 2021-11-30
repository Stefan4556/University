bits 32 

global start        

extern exit,scanf,printf,fprintf              
import exit msvcrt.dll  
import scanf msvcrt.dll
import printf msvcrt.dll           

segment data use32 class=data

    nume_fisier times 101 db 0
    caracter_consola dd 0
    nume_fisier_scriere db "output.txt",0
    mod_accesare_citire db "r",0
    mod_accesare_scriere db "w",0
    citire_fisier db "%s",0
    citire_caracter db "%c",0
    descriptor dd -1
    descriptor2 dd -1
    caracter dd 0
    sir_nou times 50 db 0
    sir_afisare times 50 db 0

segment code use32 class=code
    start:
    
        push dword nume_fisier
        push dword citire_fisier
        call [scanf]
        add esp,4*2
        
        push dword caracter_consola
        push dword citire_caracter
        call [scanf]
        add esp,4*2
        
        push dword mod_accesare_citire
        push dword nume_fisier
        call [fopen]
        add esp,4*2
        
        cmp eax,0
        je sfarsit
            
            mov [descriptor],eax
            
            push dword mod_accesare_scriere
            push dword nume_fisier_scriere
            call [fopen]
            add esp,4*2 ; deschidem cel de al doilea fisier
            
            cmp eax,0
            je sfarsit1
            mov [descriptor2],eax
            
            initializare:
                
                mov edi,sir_nou
                
            citire:
                
                push dword caracter
                push dword citire_caracter
                push dword [descriptor]
                call [fscanf]
                add esp,4*3     ; ne ocupam cu citirea cate unui caracter
                
                cmp eax,-1  ; daca este -1 trebuie sa iesim
                je afara
                
                mov eax,[caracter]
                cmp eax," "
                je este_spatiu
                jne nu_este_spatiu
                este_spatiu:
                    mov al,[edi+1]
                    cmp al,[caracter_consola]
                    jne sari    ; daca nu este egal o sa sarim peste el ca nu trb sa l afisam
                        mov al,0
                        stosb
                        mov [sir_nou],edi
                        
                        push dword sir_nou
                        call [fprintf]
                        add esp,4
                    sari:
                    jmp initializare 
             
             jmp citire
             
           afara:
            
        sfarsit:
    
        push    dword 0      
        call    [exit]       
