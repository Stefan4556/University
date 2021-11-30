bits 32
;Sa se scrie un program care citeste cifre pana cand se citeste caracterul '!'(din consola).
;Sa se formeze si sa se afiseze cel mai mare numar format doar cu cifrele pare citite de la 
;tastatura(intr-un fisier 'output.txt').
global start        

extern exit,scanf,fprintf,fopen,fclose              
import exit msvcrt.dll
import scanf msvcrt.dll
import fprintf msvcrt.dll   
import fopen msvcrt.dll
import fclose msvcrt.dll 

segment data use32 class=data
    
    cifra dd 0
    sir times 101 dd 0
    format_citire db "%c",0
    format_afisare db "%d",0
    fisier_output db "output_!.txt",0
    acces_fisier db "w",0
    lungime dd 0
    copie_lungime dd 0
    variabila dd 0
    descriptor dd 0
    
segment code use32 class=code
    start:
        
        push dword acces_fisier
        push dword fisier_output
        call [fopen]
        add esp,4*2
        
        cmp eax,0
        je sfarsit2
        
        mov [descriptor],eax
        
        mov edi,sir
        
        citeste:
        ; ne ocumpam de citirea cifrei
        
            push dword cifra
            push dword format_citire
            call [scanf]
            add esp,4*2
            
            mov eax,0
            mov edx,0
            mov eax,[cifra]
            
            cmp eax," "
            je continua
            
            cmp eax,"!"
            je afara
            
            sub eax,"0"
            mov [variabila],eax
            cdq
            mov ebx,2
            div ebx
            cmp edx,0
            jne continua
            ;retinem cifra
            mov eax,[variabila]
            stosd
            inc dword[lungime]
            continua:
        jmp citeste
        
        afara:
        
        mov edx,[lungime]
        cmp edx,0
        je sfarsit3
        
        ; trebuie sa sortam sirul dupa care sa-l afisam
        
        mov edx,1
        while:
            cmp edx,0
            jz sfarsit
            mov edx,0
            mov esi,sir
            mov ecx,[lungime]
            sub ecx,1
            for:
                mov eax,[esi]
                cmp eax,[esi+4]
                jae next
                mov ebx,[esi+4]
                mov [esi],ebx
                mov [esi+4],eax ; interschimbare
                mov edx,1
                next:
                    add esi,4
            loop for
            jmp while
            sfarsit:
        
        mov ecx,[lungime]
        mov esi,sir
        repeta:
            
            lodsd
            mov [copie_lungime],ecx
            mov [variabila],eax
            
            push dword [variabila]
            push dword format_afisare
            push dword [descriptor]
            call [fprintf]
            add esp,4*3
            
            mov ecx,[copie_lungime]
            
        loop repeta
        
        sfarsit3:
        
            push dword [descriptor]
            call [fclose]
            add esp,4
        
        sfarsit2:
        
        push    dword 0      
        call    [exit]       
