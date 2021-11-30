bits 32 

global start        

extern exit,printf               
import exit msvcrt.dll
import printf msvcrt.dll                            

segment data use32 class=data

    sir dd 125,215,-125,355
    lungime_sir equ ($-sir)/4
    rez times lungime_sir*2 dw 0
    lungime_sir_rez dd 0
    adresa_rezultat dd 0
    copie_word_low dw 0
    copie_word_high dw 0
    cifra equ 5
    format_afisare db "Rezultatul impartirii maximului=%d si al minimului=%d este cat=%d si rest=%d",0
    copie_contor dd 0
    nr dw 0
    maxim dd 0
    minim dd 0

segment code use32 class=code
    start:
    
    mov esi,sir
    mov edi,rez
    mov [adresa_rezultat],edi
    mov ecx, lungime_sir
    mov bx, 10
    jecxz sfarsit_int  ; daca ecx = 0 sarim la final
    
    repeta:
        
        lodsd   ; incarcam cate un dword din sir
        cmp eax,0
        jl continua    ; daca eax e mai mic decat 0 mergem mai departe
        
        mov [copie_word_low],ax
        ror eax,16
        mov [copie_word_high],ax
        cwd ; convertim ax la dx : ax pentru a putea realiza imaprtirea
        idiv bx     ; in ax se afla cat-ul si in dx - restul
        cmp dx,cifra
        je salveaza
        jne continua_2
        
        salveaza:
            mov ax,[copie_word_high]
            stosw   ; stocam word-ul high
            inc dword [lungime_sir_rez]
        
        continua_2: ; ne ocupam de word-ul low acum
        
        mov ax,[copie_word_low]
        cwd     ; ax -> dx : ax pentru a putea face imp
        idiv bx ; in dx - rest si ax - cat
        cmp dx,cifra
        je salveaza_2
        jne continua
        
        salveaza_2:
            
            mov ax,[copie_word_low]
            stosw   ; salvam word-ul low
            inc dword [lungime_sir_rez]
            
        continua:
        
    loop repeta
    
    jmp eticheta
        sfarsit_int:
            jmp sfarsit
    eticheta:
    
    mov esi,rez
    mov ecx,[lungime_sir_rez]
    lodsw
    mov [maxim],ax
    mov [minim],ax
    dec ecx
    
    repeta1:
    
        lodsw
        cmp ax,[maxim]
        jae actualizeaza_maxim
        jl  continua1
        actualizeaza_maxim:
            mov [maxim],ax
        continua1:
        cmp ax,[minim]
        jle actualizeaza_minim
        ja continua2
        actualizeaza_minim:
            mov [minim],ax
        continua2:
    
    loop repeta1
    
    mov eax,[maxim]
    cdq
    mov ebx,[minim]
    idiv ebx    ; eax - cat si edx - rest
    
    push edx
    push eax
    push ebx
    push dword [maxim]
    push dword format_afisare
    call [printf]
    add esp,4*5
    
    sfarsit:
    
        push    dword 0      
        call    [exit]       
