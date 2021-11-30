% cauta(L, E) - rolul acestei functii este de a cauta elementul E in
%               lista L
% cauta(l1,...,ln,E) = {   Fals               , n = 0
%                      {   Adevarat           , n > 0 si l1 = E
%                      {   cauta(l2,...,ln,E) , altfel
% model de flux(i, i), determinist
cauta([E|_],E).
cauta([H|T],E):-H\=E,cauta(T,E).

% transforma(L, C) - rolul acestei functii este de a transforma lista
%                    trimisa ca si parametru in multime
% transforma(l1,...,ln,C) = {   []                             , n = 0
%                           { l1 + transforma(l2,...,ln,l1 + C), n > 0
%                           {                   si cauta(C, l1) = fals
%                           { transforma(l2,...,ln)            , altfel
% model de flux(i, i, o), determinist
transforma([],_,[]). %ramura 1
transforma([H|T],C,[H|O]):-not(cauta(C,H)),
                   transforma(T,[H|C],O).
                   % ramura 2
transforma([H|T],C,O):-cauta(C,H),
                     transforma(T,C,O).
                    % ramura 3
% transforma_main(H) - functia ce apeleaza functia auxiliara transforma,
%                      ce transforma o lista intr-o multime
% transforma_main(H) = transforma(H, [])
% model de flux(i, o), determinist
transforma_main(H,O):-transforma(H,[],O). %functia mama

test:-transforma_main([1,2,3,1,2],[1,2,3]),
      transforma_main([1,1,1,2,2,3,3,1,2],[1,2,3]),
      transforma_main([1,2,3,3,2,1],[1,2,3]),
      transforma_main([],[]).


