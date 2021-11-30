bits 32

; Structura Stiva
; [EBP + 0] - adresa pentru apelant
; [EBP + 4] - adresa de return
; [EBP + 8] - adresa sirului rezultat
; [EBP + 12] - adresa sirului s1
; [EBP + 16] - adresa sirului s2
; [EBP + 20] - lungimea minima pentru a stii cand se ne oprim
; [EBP + 24] - lungimea s1
; [EBP + 28] - lungimea s2

global _cautaresufix

;char cautaresufix(char rezultat[101],char s1[101],char s2[101],char s3[101],int lungime_minima,int ls1,int ls2);

segment data public data use32
    
    adresa_s1 dd 0
    adresa_s2 dd 0
    ;sir resb 20
    
segment code public code use32

_cautaresufix:

    push ebp
    mov ebp, esp
    
    pushad  ; punem registrii pe stiva pentru a nu influenta valoriile acestora cu care au venit din programul c
    
    mov eax,[EBP + 12]
    add eax,[EBP + 24]
    mov [adresa_s1],eax ; punem adresa de final a lui s1
    
    mov eax,[EBP + 16]
    add eax,[EBP + 28]
    mov [adresa_s2],eax ; punem adresa de final a lui s2
    
    mov ecx,[EBP + 20]  ; lungimea minima a unuia dintre siruri
    
    mov edi,[EBP + 8]   ; adresa de inceput a sirului rezultat
    
    
    mov edx,0
    
    Repeta:
    
        std
        mov esi,[adresa_s1]
        lodsb
        mov bl,al   ; bl = caracter din s1
        mov [adresa_s1],esi
        
        mov esi,[adresa_s2]
        lodsb   ; al = caracter din s2
        mov [adresa_s2],esi
        
        cmp bl,al
        je adauga_caracter
        jne sfarsit ; inseamna ca nu mai avem un sufix comun
        
        adauga_caracter:
            
            cld
            stosb
     
    Loop Repeta
    
    sfarsit:
    
    ;mov [sir],edi
    
    popad  ; punem valorile inapoi pentru a ne asigura ca programul o sa ruleze corect in continuare
    
    ;mov eax,[sir]
    
    mov esp, ebp
    pop ebp
    
    ret
