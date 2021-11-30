bits 32 

global start        

extern exit,fscanf,fprintf,fclose,fopen               
import exit msvcrt.dll     
import fscanf msvcrt.dll
import fprintf msvcrt.dll
import fclose msvcrt.dll
import fopen msvcrt.dll 

segment data use32 class=data

    fisier1 db "input_n-i.txt",0
    acces1 db "r",0
    descriptor1 dd -1
    fisier2 db "output_n-i.txt",0
    acces2 db "w",0
    descriptor2 dd -1
    sir times 101 db 0
    lungime dd 0
    format_caracter db "%c",0
    caracter dd 0
    jumatate dd 0
    copie_ecx dd 0

segment code use32 class=code
    start:

        push dword acces1
        push dword fisier1
        call [fopen]
        add esp,4*2
        
        cmp eax, 0
        je final
        
            mov [descriptor1],eax
            mov edi,sir
            
            citire:
                
                push dword caracter
                push dword format_caracter
                push dword [descriptor1]
                call [fscanf]
                add esp,4*3
                
                cmp eax,-1
                je afara
                
                mov eax,0
                mov eax,[caracter]
                stosb
                inc dword[lungime]
                
             jmp citire
             afara:
             
            push dword [descriptor1]
            call [fclose]
            add esp,4
             
             push dword acces2
             push dword fisier2
             call [fopen]
             add esp,4*2
             
             cmp eax,-1
             je final
             
             mov [descriptor2],eax
             
             mov esi,0
             
             mov eax,[lungime]
             mov edx,0
             mov ebx,2
             div ebx
             mov [jumatate],eax
             
             mov ebx,0  ; cu ajutorul lui ebx aflam daca este par sau impar indicele
             
             mov esi,0
             
             afiseaza:
             
                    cmp ebx,0
                    je par_schimb
                    jne nu_par
                    par_schimb:
                        mov ecx,[lungime]
                        sub ecx,esi
                        mov al,[sir+esi]
                        mov dl,[sir+ecx-1]
                        mov [sir+ecx-1],al
                        mov [sir+esi],dl
                        mov ebx,1
                        jmp continua
                    nu_par:
                        mov ebx,0
                    continua:
                    inc esi
                    cmp esi,[jumatate]  ; pana la jumatate
                
            jb afiseaza
            
            mov ecx,[lungime]
            mov esi,sir
            mov al,0
            stosb
            
            push dword sir
            push dword [descriptor2]
            call [fprintf]
            add esp,4*2
            
            ; afisare_caractere:
                ; mov eax,0
                ; lodsb 
                ; mov [caracter],eax
                ; mov [copie_ecx],ecx
                ; push dword [caracter]
                ; push dword format_caracter
                ; push dword [descriptor2]
                ; call [fprintf]
                ; add esp,4*3
                ; mov ecx,[copie_ecx]
             ; loop afisare_caractere
            
            push dword [descriptor2]
            call [fclose]
            add esp,4
            
        final:

        push    dword 0    
        call    [exit]       
