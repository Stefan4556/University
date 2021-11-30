;(load "Laboratoare/L2/1.lisp")

;1. Se da un arbore de tipul (1). Sa se afiseze calea de la radacina pana la un
;   nod x dat.
;   Reprez (1): (A 2 B 0 C 2 D 0 E 0)
;
;   O sa definim o functie cauta ce verifica daca un element exista intr-o lista liniara
;   cauta(l1,...,ln, el) = {    false               , n = 0
;                          {    true                , n > 0 si el = l1
;                          {    cauta(l2,...,ln, el), altfel
;
;   cauta(l;List, el:atom)

(defun cauta (l el)

    (cond 
        ((null l)

            NIL
        )

        ((equal (car l) el)

            T
        )

        (t 
            (cauta (cdr l) el)
        )     
    )
)

(defun testCauta ()

    (AND
    
        (equal (cauta `() 1) NIL)
        (equal (cauta `(A 2 B 0 C 2 D 0 E 0) `F) NIL)
        (equal (cauta `(A 2 B 0 C 2 D 0 E 0) `E) T)
        (equal (cauta `(1 2 3) 1) T)
        (equal (CDDR `(1 2 3)) `(3))
    )
)

;   O sa definim o functie ce determina subarborele stang al unui arbore
;
;   stang(l1, ..., ln) = parcurg_stanga(l3, ..., ln, 0, 0)
;   stang(l:List)
;
;   Functia efectiva de calculare este urmatoarea
;   nr_vf = numar varfuri
;   nr_m = numar muchii
;   parcurg_stanga(l1, l2, ..., ln, nr_vf, nr_m) = {    []                                                      , n =  0
;                                                  {    []                                                      , nr_vf = nr_m + 1
;                                                  {    l1 + l2 + parcurg_stanga(l3, ..., ln, nr_vf + 1, nr_m + l2)    , altfel
;   parcurg_stanga(l:List, nr_vf:int, nr_m:int)

(defun parcurg_stanga (l nr_vf nr_m)

    (cond

        ((null l)
            NIL
        )

        ((equal nr_vf (+ 1 nr_m))
            NIL
        )

        (t
            (cons 
                (car l) 
                (cons (cadr l) 
                    (parcurg_stanga 
                        (cddr l)
                        (+ 1 nr_vf)
                        (+ nr_m (cadr l)) 
                    )
                )
            )
        )
    )
)

(defun stang (l)

    (parcurg_stanga (cddr l) 0 0)
)

(defun testStanga ()

    (AND
        (equal (stang `(a 2 b 2 c 1 i 0 f 1 g 0 d 2 e 0 h 0)) `(b 2 c 1 i 0 f 1 g 0))
        (equal (stang `()) NIL)
        (equal (stang `(c 1 i 0)) `(i 0))
    )
)

;   O sa definim o functie ce determina subarborele drept al unui arbore
;
;   drept(l1, ..., ln) = parcurg_dreapta(l1, ..., ln, 0, 0)
;   drept(l:List)
;
;   Functia efectiva de calculare este urmatoarea
;   nr_vf = numar varfuri
;   nr_m = numar muchii
;   parcurg_dreapta(l1, l2, ..., ln, nr_vf, nr_m) = {    []                                                      , n =  0
;                                                   {    l                                                      , nr_vf = nr_m + 1
;                                                   {    parcurg_dreapta(l3, ..., ln, nr_vf + 1, nr_m + l2)     , altfel
;   parcurg_dreapta(l:List, nr_vf:int, nr_m:int)

(defun parcurg_dreapta (l nr_vf nr_m)

    (cond

        ((null l)
            NIL
        )

        ((equal nr_vf (+ 1 nr_m))
            l
        )

        (t
            (parcurg_dreapta 
                (cddr l)
                (+ 1 nr_vf)
                (+ nr_m (cadr l)) 
            )
        )
    )
)

(defun drept (l)

    (parcurg_dreapta (cddr l) 0 0)
)

(defun testDreapta ()

    (AND
        (equal (drept `(a 2 b 2 c 1 i 0 f 1 g 0 d 2 e 0 h 0) ) `(d 2 e 0 h 0) )
        (equal (drept `(f 1 g 0)) NIL)
        (equal (drept `(A 2 B 0 C 2 D 0 E 0)) `(C 2 D 0 E 0))
        (equal (drept `()) NIL)
    )
)

;   Definim functia ce o sa determine drumul de la radacina la un nod primit ca si parametru
;    Ca si conditii el exista in l, acest lucru fiind deja verificat in functia in care apelam aceasta functie
;   drumRadacinaNod(l1, ..., ln, el) = {      [el]            , cauta(stang(l), el) = false si cauta(stang(l), el) = false
;                                    {  l1 + drumRadacinaNod, cauta(stang(l), el) = true 
;                                    {  l1 + drumRadacinaNod, cauta(stanga(l), el), altfel
;   drumRadacinaNod(l:List, el:atom) 
(defun drumRadacinaNod (l el)

    (cond

        ((AND
         (equal (cauta (stang l) el) NIL)
         (equal (cauta (drept l) el) NIL)
         )
            (list el)
        )

        ((equal (cauta (stang l) el) T)
            (cons (car l) (drumRadacinaNod (stang l) el))
        )
        (t
            (cons (car l) (drumRadacinaNod (drept l) el))
        )
    )
)

(defun testDrumRadacinaNod ()

    (AND
        (equal (drumRadacinaNod `(A 2 B 0 C 2 D 0 E 0) `B) `(A B))
        (equal (drumRadacinaNod `(A 2 B 0 C 2 D 0 E 0) `E) `(A C E))
        (equal (drumRadacinaNod `(a 2 b 2 c 1 i 0 f 1 g 0 d 2 e 0 h 0) `G) `(A B F G))
        (equal (drumRadacinaNod `(a 2 b 2 c 1 i 0 f 1 g 0 d 2 e 0 h 0) `i) `(A B C I))
    )
)

;   Definim functia main, ce cauta in primul rand daca elementul cautat de noi exista, in caz afirmativ determina drumul de la radacina la acesta
;   main(l, el) = {   false                   , cauta(l, el) = false    || cazul in care lista este vida este prins aici
;                 {   drumRadacinaNod(l, el)  , altfel
;   main(l:List, el:atom)
(defun main (l el)

    (cond

        ((equal (cauta l el) NIL)
            NIL
        )

        (t
            (drumRadacinaNod l el)   
        )
    )
)

(defun testMain ()

    (AND
        (equal (main `(A 2 B 0 C 0) `E) NIL)
        (equal (main `(A 2 B 0 C 2 D 0 E 0) `B) `(A B))
        (equal (main `(A 2 B 0 C 2 D 0 E 0) `E) `(A C E))
        (equal (main `(a 2 b 2 c 1 i 0 f 1 g 0 d 2 e 0 h 0) `G) `(A B F G))
        (equal (main `(a 2 b 2 c 1 i 0 f 1 g 0 d 2 e 0 h 0) `i) `(A B C I))
    )
)

(defun testeFunctii ()

    (AND
        (testCauta)
        (testStanga)
        (testDreapta)
        (testDrumRadacinaNod)
        (testMain)
    )
)