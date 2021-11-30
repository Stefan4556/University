bits 32

global _conversie_string          

segment data public data use32
    
    sir db '10100111b', '01100011b', '110b', '101011b'
    lungime equ 4   ; daca modificam sirul sir trebuie sa modificam si lungimea acestuia in cazul in care adaugam / stergem un string
    sir_rezultat times lungime db 0
    
segment code public code use32
    _conversie_string:
        
    push ebp
    mov ebp, esp
    
    pushad
    
    mov esi,sir ; punem in esi sirul nostru
    
    mov edi,[ebp+8] ; punem in edi sirul in care o sa stocam int(string)
    
    mov ecx, lungime ; punem in ecx lungimea vectorului
    
    mov eax,ecx ; formam v[0]
    
    stosd   ; salvam pe prima pozitie din vector lungimea sirului de cuvinte

    mov eax,0
    
    Repeta:
        
        mov bl,0 ; aici o sa salvam rezultatul curent
        
        repeta1: ;parcurgem cate un string din sir pana la caracterul b
        
        lodsb ; punem in al cate un caracter
        cmp al,"b"
        je continua ; daca nu e egal cu b inseamna ca suntem pe o cifra binara
        
        sub al,"0" ; transforma cifra din string in int
        
        shl bl,1   ; shiftam la stanga
        
        add bl,al  ; actualizam rezultatul
        
        jmp repeta1
        
        continua:
        mov eax,0
        mov al,bl   ; punem rezultatul in al pentru a-l stoca
        stosd
        
    Loop Repeta
    
    ;mov eax,edi     ; punem in eax vectorul rezultat
    popad
    
    mov esp, ebp
    pop ebp

    ret