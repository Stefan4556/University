bits 32

global start        

extern exit,fopen,fread,fprintf,fclose,printf,fscanf               
import exit msvcrt.dll
import fopen msvcrt.dll
import fread msvcrt.dll
import fclose msvcrt.dll
import fprintf msvcrt.dll
import printf msvcrt.dll
import fscanf msvcrt.dll                         

segment data use32 class=data
    
    nume_fisier db "invatam.txt",0
    mod_acces db "r+",0     ; acest mod de acces este specific pentru citire si scriere in fisierul existent 
    descriptor dd -1
    format_afisare db "%d",0
    sir times 101 db 0
    format_afisare_ecran db "%s",10,0
    format_citire db "%d",0
    variabila dd 0
    
segment code use32 class=code
    start:
    
    ; pentru a deschide un fisier trebuie sa folosim: 
    ; fopen(nume_fisier,mod_acces)
    push dword mod_acces
    push dword nume_fisier
    call [fopen]
    add esp,4*2     ; ideea este ca in eax se pune valoarea descriptorului, daca aceasta este 0 inseamna ca fisierul
                    ; nu a fost deschis cu succes
    cmp eax,0   ; verificam daca a fost deschis cu succes fisierul
    je sfarsit
    mov [descriptor],eax
    
    ; pentru a citi dintr-un fisier trebuie sa folosim: 
    ; fread(sir,dimens unui element - in general 1, numarul maxim de elemente citite, descriptorul)
    push dword [descriptor]
    push dword 101
    push dword 1
    push dword sir
    call [fread]
    add esp,4*4     ; dupa aceasta secventa de cod ar trb ca in eax sa se afle numarul de elemente din sir
                    ; daca val lui eax este mai mica decat 101 in cazul de fata, fie a intampinat o eroare,
                    ; fie s-a ajuns la finalul fisierului
    
    push dword sir
    push dword format_afisare_ecran
    call [printf]
    add esp,4*2     ; facem afisare pentru a verifica daca continutul citit din fisierul invatam.txt este corect
    
    ; pentru a scrie intr-un fisier trebuie sa folosim:
    ; fprintf(descriptor,format afisarii, var1, const2,...)
    push dword 50
    push dword format_afisare
    push dword [descriptor]
    call [fprintf]
    add esp,4*3     ; dupa aceasta secventa de cod ar trb ca in fisier sa fie scris 50
    
    ; pentru a citi un singur caracter/ numar din fisier trebuie sa folosim:
    ; fscanf(descriptor,format,adresa unde o sa fie salvat numarul/caracterul)

    ; push dword variabila
    ; push dword format_citire
    ; push dword [descriptor]
    ; call [fscanf]
    ; add esp,4*3   ; pune -1 in eax daca nu mai are ce sa citeasca
    
    ; push dword [variabila]
    ; push dword format_citire
    ; call [printf]
    ; add esp,4*2
    
    ; pentru a inchide un fisier trebuie sa folosim:
    ; fclose(descriptor)
    push dword [descriptor]
    call [fclose]
    add esp,4*1 ; dupa aceasta secventa de cod fisierul corespunzator descriptorului ar trb sa se fi inchis
    
    sfarsit:
        push    dword 0      
        call    [exit]       
