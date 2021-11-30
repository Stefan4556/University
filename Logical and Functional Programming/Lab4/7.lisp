; DE SCRIS LA FIECARE FUNCTIE
; descriere a functiei
; model matematic
; ce argumente avem
; teste

; (load "Laboratoare/Laborator1/7.lisp") 
; Problema 7

; a) Sa se scrie o functie care testeaza daca o lista este liniara

; Aceasta functie verifica daca o lista este liniara sau nu
;
; 7a(l1,l2,...,ln) = {   true            , n = 0
;                    {   false           , n > 0 si l1 e lista
;                    {   7a(l2,...,ln)   , altfel
;  
; 7a(L:lista) si returneaza T - Adevarat sau NIL - Fals

(defun 7a (l)

    (cond 

        ((null l) t)
        ((LISTP (car l)) NIL)
        (t (7a (cdr l)))
    )
)

(defun test7a ()

        (AND
            (equal (7a `(1 2 3)) T)
            (equal (7a `(1 2 3 (4 5))) NIL)
            (equal (7a `((1))) NIL)
            (equal (7a `(1)) T)
        )
)

;=================================================================================================================================================================================
; b) Definiti o functie care substituie prima aparitie a unui element intr-o lista data.
;
; O sa definim o functie cauta, ce se ocupa cu cautarea unui element intr-o lista eterogena
;
; cauta(l1,...,ln, el) = {   false                                      , n = 0
;                        {   true                                       , l1 = el, l1 e numar
;                        {   cauta(l1, el) sau cauta(l2,...,ln, el)     , l1 e lista    
;                        {   cauta(l2,...,ln, el)                       , altfel
;
; cauta(l:list, el: int)

(defun cauta (l el)

    (cond
    
        ((null l) NIL)
        ( (and (atom (car l) ) (equal (car l) el) ) t)
        ( (LISTP (car l) ) (OR (cauta (car l) el) (cauta (cdr l) el)))
        (t (cauta (cdr l) el))
    )
)

(defun testCauta ()

    (AND

        (equal (cauta `(1 2 3) 1) T)
        (equal (cauta `((2 (3 (1))) 2 3) 1) T)
        (equal (cauta `((2 (3 (4))) 2 3) 1) NIL)
        (equal (cauta `() 1) NIL)
    )
)

; Aceasta functie substitutie prima aparitie a unui element cu o valoare primita ca si parametru
;
; 7b(l1,...,ln,flag,nr,sub) = {     []                                                    , n = 0
;                             {   sub + 7b(l2,...,ln, true, nr, sub)                      , l1 = nr, flag = false, n > 0
;                             {   7b(l1, flag, nr, sub) + 7b(l2,...,ln, true, nr, sub)    , l1 - list, flag = false, cauta(l1, nr) = true, n > 0      
;                             {   l1 + 7b(l2,...,ln, flag, nr, sub)                       , altfel
;
; 7b(L: list, flag : NIL / T, nr: int, sub: int)

(defun 7b (l flag nr sub)   ; poate facem si varianta 2 sa returnam cand deja am substituit si scapam de flag

    (cond

        ((null l) 

                (list)
        )
        ((AND 
            (equal (car l) nr) 
            (null flag))

                (cons sub (7b (cdr l) t nr sub))
        )
        ((AND 
            (LISTP (car l)) 
            (null flag) 
            (cauta (car l) nr)) 
            
                (cons 
                    (7b 
                        (car l) 
                        flag 
                        nr 
                        sub
                    ) 

                    (7b 
                        (cdr l) 
                        t 
                        nr 
                        sub)
                )
        )
        (t (cons(car l)(7b (cdr l) flag nr sub)))
    )
)

(defun test7b ()

    (AND
    
        (equal (7b `(1 2 3 1) NIL 5 4) `(1 2 3 1))
        (equal (7b `(1 1 1 1) NIL 1 4) `(4 1 1 1))
        (equal (7b `(1) NIL 1 4) `(4))
        (equal (7b `() NIL 1 4) NIL)
        (equal (7b `( (2(3(4(1)))) 1 1 1) NIL 1 4) `((2 (3 (4 (4)))) 1 1 1))
        (equal (7b `( (2(3(4(1 1) 1) 1) 1) 1 1 1) NIL 1 4) `((2 (3 (4 (4 1) 1) 1) 1) 1 1 1))
    )
)

;=================================================================================================================================================================================
; c) Sa se inlocuiasca fiecare sublista a unei liste cu ultimul ei element. Prin sublista se intelege elementul de pe primul nivel, care este lista.
;
; Rolul acestei functii este de a determina ultimul element dintr-o lista - functie auxiliara
; detUltElem(l1,...,ln) = {     l1                      , n = 1 si l1 e atom
;                         {     detUltElem(l1)          , n = 1 si l1 e lista
;                         {     detUltElem(l2,...,ln)   , altfel (n > 1)
;
; detUltElem(l : list)

(defun detUltElem (l)   ; grija la cazul in care lista este vida si la elementele ce contin NIL

    (cond
    
        (( AND (null (cdr l)) (atom(car l))) (car l))
        (( AND (null (cdr l)) (LISTP(car l))) (detUltElem (car l))) 
        (t (detUltElem(cdr l)))
    )
)

(defun testDetUltElem ()   

    (AND
        (equal (detUltElem `()) NIL)
        (equal (detUltElem `(1 2 3)) 3)
        (equal (detUltElem `(1 2 (3 4 (5 (6))))) 6)
        (equal (detUltElem `(1 (3 4) (3 4 (5 (6 (7 (8 (9)))))))) 9)
    )
)

; Rolul acestei functii este sa inlocuiasca fiecare sublista cu ultimul ei element, aceasta operatie fiind aplicata pentru fiecare sublista dintr-o sublista
;
; 7c(l1,...,ln) = {         []                          , n = 0
;                 {   l1 + 7c(l2,...,ln)                , n > 0 si l1 e atom
;                 {   detUltElem(l1) + 7c(l2,...,ln)    , altfel (n > 0 si l1 e lista)
;
; 7c(l : list)

(defun 7c (l)

    (cond

        ((null l) (list))
        ((atom (car l)) (cons (car l) (7c(cdr l))))
        (t (cons (detUltElem(car l)) (7c(cdr l))))
    )
)

(defun test7c ()

    (AND
        (equal (7c `(a (b c) (d (e (f) ) ) ) ) `(A C F))
        (equal (7c `(((((((a))))))) ) `(A))
        (equal (7c `((((((())))))) ) `(NIL))
        (equal (7c `(1 2 a b)) `(1 2 A B))
    )
)

;=================================================================================================================================================================================
; d) Definiti o functie care interclaseaza fara pastrarea dublurilor doua liste liniare sortate.
;
; Rolul acestei functii este de a interclasa 2 liste liniare sortate
;
; 7d(l11, ..., l1n1, l21, ..., l2n2) = {                []                                  , n1 = 0 si n2 = 0  || ulterior mi-am dat seama ca nu era necesara aceasta ramura
;                                      {                l1                                  , n1 != 0 si n2 = 0
;                                      {                l2                                  , n1 = 0 si n2 != 0
;                                      {  l11 + 7d(l12,...,l1n1, l21,...,l2n2)              , n1 != 0, n2 != 0, l11 < l21
;                                      {  l21 + 7d(l11,...,l1n1, l22,...,l2n2)              , n1 != 0, n2 != 0, l21 < l11
;                                      {  l11 + 7d(l12,...,l1n1, l22,...,l2n2)              , altfel(n1 != 0, n2 != 0, l11 = l21)
;
; 7d(l1 : list, l2 : list)
;
; Teste:
; - (7d `(1 3 5) `(2 4 6)) = (1 2 3 4 5 6)
; - (7d `() `(2 4 6)) = (2 4 6)
; - (7d `(2 3 5) `()) = (2 3 5) 
; - (7d `() `()) = NIL
; - (7d `(2 3 5) `(1 4 5)) = (1 2 3 4 5)
; - (7d `(1 2 3) `(1 2 3)) = (1 2 3)

; (INTERCL '(1 1 2 4) '(1 1 3 5)) - asteapta rasp legat de cazul asta, o varianta usoara ar fi sa mai ai un argument - previous ce sa retina ultimul elem adaugat in lista rez, dar 
; ar trb sa stergem din cele 2 liste elementul respectiv || SAU convertim lista intr o lista fara elemente duplicate
(defun 7d (l1 l2)

    (cond
    
        ((AND (null l1)(null l2)) (list))
        ((AND (null l2)(not(null l1))) l1)
        ((AND (null l1)(not(null l2))) l2)
        ((< (car l1) (car l2)) (cons(car l1)(7d (cdr l1) l2)))
        ((< (car l2) (car l1)) (cons(car l2)(7d l1 (cdr l2))))
        (t (cons(car l1)(7d (cdr l1) (cdr l2))))
    )
)

(defun test7d ()

    (AND

        (equal (7d `(1 3 5) `(2 4 6)) `(1 2 3 4 5 6))
        (equal (7d `() `(2 4 6)) `(2 4 6))
        (equal (7d `(2 3 5) `()) `(2 3 5))
        (equal (7d `() `()) NIL)
        (equal (7d `(2 3 5) `(1 4 5)) `(1 2 3 4 5))
        (equal (7d `(1 2 3) `(1 2 3)) `(1 2 3))
    )
)

; Functie pentru testarea tuturor functiilor folosite in cadrul problemei 7
(defun test7 ()

    (AND

        (test7a)
        (test7b)
        (test7c)
        (test7d)
        (testCauta)
        (testDetUltElem)
    )
)