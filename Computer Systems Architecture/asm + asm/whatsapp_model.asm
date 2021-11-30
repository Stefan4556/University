bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    a1 db "256,-256"
    a2 dw 256,256h
    a3 dw $-a2
    a4 equ -256/4
    a5 db 128>>1,-128<<1
    a6 dw a2-a5,~(a2-a5)
    ;a7 dd [a2],!a2
    a8 dd 256h^256,256256h
    a9 dd ($-a8) + (a10-$)
    a10 dw -255,256h
    a11 dw 256-256h
    a12 times 4 dw 256
    ;a13 dw times 4 -128
    a14 dw -256
    a15 times 2 dd 12345678h
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
        ; push ebp
        ; mov ebp,esp
        ; mov ebp,[ebp]
        ; mov ebx,[ebp]
        ; mov [esp],ebx
        lea ebx,[esp+4]
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
