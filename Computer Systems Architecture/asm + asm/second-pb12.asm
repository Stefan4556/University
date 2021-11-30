bits 32 

; stiva - adresa_retur - [ESP]
      ; - s1 - [ESP + 4]
      ; - s2 - [ESP + 8]
      ; - rez - [ESP + 12]
      ; - len - [ESP + 16]      

extern printf               
import printf msvcrt.dll
global concatenare    

segment data use32 class=data public

    adresa_s1 dd 0
    adresa_s2 dd 0
    adresa_r dd 0
    format_afisare_1 db "Prima varianta de concatenare este %s",10,0
    format_afisare_2 db "A doua varianta de concatenare este %s", 0
    
segment code use32 class=code public
    
    concatenare:
        
        ; punem s1 pe poz pare si s2 pe poz impare
        mov ecx,[ESP + 16]
        mov edi,[ESP + 12]
        
        mov eax,[ESP + 4]
        mov [adresa_s1],eax ;retinem adresa lui s1
        
        mov eax,[ESP + 8]
        mov [adresa_s2],eax ;retinem adresa lui s2
        
        mov [adresa_r],edi  ;retinem adresa de inceput a lui rez pentru a putea afisa sirul la final
        
        ;interclasam cele 2 siruri: un element din s1, unul din s2
        cld 
        repeta1:
        mov esi,[adresa_s1]
        movsb
        mov [adresa_s1],esi
        
        mov esi,[adresa_s2]
        movsb
        mov [adresa_s2],esi
        
        loop repeta1
        
        ; ne ocupam de afisarea primului caz
        push dword [adresa_r]
        push dword format_afisare_1
        call [printf]
        add esp,4*2
        
        ; punem s1 pe poz impare si s2 pe poz pare
        
        mov edi,[ESP + 12]
        mov ecx,[ESP + 16]
        
        mov eax,[ESP + 4]
        mov [adresa_s1],eax ;retinem adresa lui s1
        
        mov eax,[ESP + 8]
        mov [adresa_s2],eax ;retinem adresa lui s2
        
        ;interclasam cele 2 siruri: un element din s2, unul din s1
        cld 
        repeta2:
        
        mov esi,[adresa_s2]
        movsb
        mov [adresa_s2],esi
        
        mov esi,[adresa_s1]
        movsb
        mov [adresa_s1],esi
        
        loop repeta2
        
        ; ne ocupam de afisarea celui de al 2 lea caz
        push dword [adresa_r]
        push dword format_afisare_2
        call [printf]
        add esp,4*2
        
        ret 4*4
        
    
        
