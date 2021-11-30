bits 32

; Structura Stiva
; [EBP + 0] - adresa pentru apelant
; [EBP + 4] - adresa de return
; [EBP + 8] - adresa sirului rez
; [EBP + 12] - adresa sirului s1
; [EBP + 16] - adresa sirului s2
; [EBP + 20] - lungimea unui sir deoarece au lungimi egale

global _concatenare

segment data public data use32
    
    adresa_s1 dd 0
    adresa_s2 dd 0

segment code public code use32
;char concatenare(char rez[],char s1[], char s2[],int lungime);
_concatenare:
    
    push ebp
    mov ebp, esp
    
    pushad ; punem registrii pe stiva pentru a nu influenta rularea programului dupa ce se termina aceasta functie, ce ii foloseste
    
    mov eax,[EBP + 12]
    mov [adresa_s1],eax ; salvam in variabila adresa lui s1
    
    mov eax,[EBP + 16]
    mov [adresa_s2],eax ; salvam in variabila adresa lui s2
    
    mov edi,[EBP + 8] ; punem in edi adresa sirului rezultat
    
    mov ecx,[EBP + 20] ; punem lungimea lui s1
    
    ; Ne ocupam de primul caz, cel cu s1 pe poz pare, s2 pe poz impare
    
    cld ; pentru a incepe de la stanga la dreapta
    
        repeta1:
    
            mov esi,[adresa_s1]
            movsb
            mov [adresa_s1],esi
            
            mov esi,[adresa_s2]
            movsb
            mov [adresa_s2],esi
        
        loop repeta1
        
    mov eax,[EBP + 12]
    mov [adresa_s1],eax ; salvam in variabila adresa lui s1
    
    mov eax,[EBP + 16]
    mov [adresa_s2],eax ; salvam in variabila adresa lui s2
    
    mov ecx,[EBP + 20] ; punem lungimea lui s1
    
    ; Ne ocupam de al doilea caz, s1 pe poz impare, s2 pe poz pare
    
        repeta2:
            
            mov esi,[adresa_s2]
            movsb
            mov [adresa_s2],esi
            
            mov esi,[adresa_s1]
            movsb
            mov [adresa_s1],esi
        
        loop repeta2
    
    popad  ; punem valorile inapoi pentru a ne asigura ca programul o sa ruleze corect in continuare
    
    mov esp, ebp
    pop ebp
    
    ret