bits 32

global start        

extern exit,scanf,printf               
import exit msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll                         

segment data use32 class=data

    format_citire db "%d",0
    mesaj_citire db "Introduceti valoarea numarului x=",0
    format_afisare db "Valoarea lui x este %d",0
    x dd 0

segment code use32 class=code
    start:
    
    ; pentru a afisa in consola un mesaj folosim:
    ; printf("mesajul e aici scris")
    push dword mesaj_citire
    call [printf]
    add esp,4*1
    
    ; pentru a citi din consola datele introduse de utilizator folosim:
    ; scanf("%d/u/x/c/s",adresa unde este salvata ceea ce citim)
    ; in cazul in care dorim sa citim mai multe variabile adaugam intre "" % si tipul de data pe care dorim sa-l citim
    ; plus adresa unde o sa fie salvat lucrul citit
    push dword x
    push dword format_citire
    call [scanf]
    add esp,4*2
    
    ; pentru a afisa in consola folosim:
    ; printf("%d/u/x/c/s",variabilele pe care dorim sa le afisam)
    push dword [x]
    push dword format_afisare
    call [printf]
    add esp,4*2
    
        push    dword 0      
        call    [exit]       
