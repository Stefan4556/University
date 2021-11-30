bits 32

; informam asamblorul ca dorim ca functia _hexa sa fie disponibila altor unitati de compilare
global _binar

; linkeditorul poate folosi segmentul public de date si pentru date din afara
segment data public data use32

; codul scris in asamblare este dispus intr-un segment public, posibil a fi partajat cu alt cod extern
segment code public code use32

; int sumaNumere(int, int)

_binar:
    ; creare cadru de stiva pentru programul apelat
    push ebp
    mov ebp, esp
	pushad
    
    mov eax, [ebp+8]  ; eax<-nr in baza 10 (x)
	cld
	mov edi, [ebp+12]
	conversie:
		cdq
		mov ecx, 2
		idiv ecx     ;eax<- x/2       edx<- x%2
		mov ebx, eax
		mov eax, edx
		stosd
		mov eax, ebx
		
		cmp eax,0
		je fin
	jmp conversie
		
	fin:
	mov eax,2
	stosd
	popad
    mov esp, ebp
    pop ebp

    ret