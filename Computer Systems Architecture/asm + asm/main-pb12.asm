bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit,concatenare,printf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll
import printf msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data public
    ; ...
        s1 db "abcd"
        len equ ($-s1)
        s2 db "efgh"
        rez times len*2 + 1 db 0
        format_afisare_1 db "Prima varianta de concatenare este %s si lungimea lui ecx este %d",0
; our code starts here
segment code use32 public class=code
    start:
        ; ...
        
        push dword len
        push dword rez
        push dword s2
        push dword s1
        call concatenare
        ;add esp,4*4
        
        ; push dword rez
        ; push dword format_afisare_1
        ; call [printf]
        ; add esp,4*2
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
