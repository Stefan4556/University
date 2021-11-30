isPrimeAux(N, DIV):-DIV * DIV > N,
                    !.
isPrimeAux(N, DIV):-DIV * DIV =< N,
                    N mod DIV =\= 0,
                    DIV1 is DIV + 2,
                    isPrimeAux(N, DIV1).

isPrimeV2(2):-!.
isPrimeV2(N):-N mod 2 =\= 0,
              N > 2,
              N < 9,
              !.
isPrimeV2(N):-N mod 2 =\= 0,
              N >= 9,
              isPrimeAux(N, 3).

