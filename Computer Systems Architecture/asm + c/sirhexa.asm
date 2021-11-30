bits 32

; informam asamblorul ca dorim ca functia _hexa sa fie disponibila altor unitati de compilare
global _hexa
extern _printf

; linkeditorul poate folosi segmentul public de date si pentru date din afara
segment data public data use32
	format db "%xh ", 0
; codul scris in asamblare este dispus intr-un segment public, posibil a fi partajat cu alt cod extern
segment code public code use32

; int sumaNumere(int, int)

_hexa:
    ; creare cadru de stiva pentru programul apelat
    push ebp
    mov ebp, esp
	pushad
    
	mov eax, [ebp + 8]
	push eax
	push dword format
	call _printf
	add esp, 4*2
	
	popad
    mov esp, ebp
    pop ebp

    ret