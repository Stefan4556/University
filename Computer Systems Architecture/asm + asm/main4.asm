bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit,hexa4,binar4,printf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll
import printf msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data public
    ; ...
    sir dd 10,20,30,2,4,6,8
    len equ ($-sir)/4
    spatiu db 10,0
    space db " ",0
    contor dd 0
; our code starts here
segment code use32 class=code public
    start:
        
    mov ebx,len
    push ebx
    push dword sir
    call hexa4
    add esp,4*2
    
    push dword spatiu
    call [printf]
    add esp,4*1
    
    mov ecx,len
    mov esi,sir
    
    repeta:
      lodsd
      
      mov [contor],ecx
      
      push eax
      call binar4
      add esp,4*1
      
      push dword space
      call [printf]
      add esp,4
      
      mov ecx,[contor]
    
    loop repeta
        
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
