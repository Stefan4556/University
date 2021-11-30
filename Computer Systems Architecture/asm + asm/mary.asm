bits 64

global start        

extern exit,gets,printf              
import exit msvcrt.dll
import gets msvcrt.dll
import printf msvcrt.dll  

segment data use64 class=data

    sir times 101 db 0
    sir_rezultat times 101 db 0
    format_citire db "%s",0     ; acesta este formatul pentru a citi un string
    mesaj_citire db "Introduceti sirul de caractere din care doriti sa eliminati semnele de punctuatie: ",0
    mesaj_afisare db "Dupa eliminarea semnelor de punctuatie sirul de caractere este: %s",0

segment code use64 class=code
    start:
        
        ; ne ocupam de afisarea unui mesaj pentru utilizator
        ; format printf(mesaj)
        push qword mesaj_citire
        call [printf]
        add rsp,8*1     ; curatare stiva
        
        ; citim sirul de caractere adica propozitia
        ; format gets(adresa unde o sa salvam propozitia)
        push qword sir
        call [gets]
        add rsp,8*1     ; curatare stiva
        
        mov esi,sir     ; punem in esi adresa propozitiei pentru a o putea parcurge
        mov edi,sir_rezultat    ; punem in edi adresa sirului rezultat
        
        mov ecx,101 ; aceasta este lungimea maxima a unei propozitii
        
        ; cu ajutorul acestui loop o sa parcurgem caracter cu caracter pentru a verifica care dintre acestea sunt caractere speciale
        ; consideram caractere speciale urmatoarele: spatiu ? . , ! : ; ' " -
        ; urmeaza sa tratam toate aceste cazuri cu cate un if
        repeta:
            
            lodsb   ; incarcam cate un caracter din sir in al
            
            cmp al," "
            je continua ; daca este egal nu mai verificam in continuare ce caracter e
            
            cmp al,"?"
            je continua ; daca este egal nu mai verificam in continuare ce caracter e
            
            cmp al,"."
            je continua ; daca este egal nu mai verificam in continuare ce caracter e
            
            cmp al,","
            je continua ; daca este egal nu mai verificam in continuare ce caracter e
            
            cmp al,"!"
            je continua ; daca este egal nu mai verificam in continuare ce caracter e
            
            cmp al,":"
            je continua ; daca este egal nu mai verificam in continuare ce caracter e
            
            cmp al,";"
            je continua ; daca este egal nu mai verificam in continuare ce caracter e
            
            cmp al,"'"
            je continua ; daca este egal nu mai verificam in continuare ce caracter e
            
            cmp al,'"'
            je continua ; daca este egal nu mai verificam in continuare ce caracter e
            
            cmp al,"-"
            je continua ; daca este egal nu mai verificam in continuare ce caracter e
            
            ; daca nu este egal o sa stocam caracterul din al in sir_rezultat
            stosb
            
            continua:
            
        loop repeta
        
        ; ne ocupam de afisarea sirului rezultat
        ; formatul lui printf("mesaj si %s",adresa sirului rezultat)
        push qword sir_rezultat
        push qword mesaj_afisare
        call [printf]
        add rsp,8*2     ; curatare stiva

        push    qword 0      
        call    [exit]       