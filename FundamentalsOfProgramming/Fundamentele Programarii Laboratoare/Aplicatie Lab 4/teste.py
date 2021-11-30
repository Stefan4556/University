"""
    Acest modul o sa contina toate functiile de testare, adica cele cu assert
"""

import cmath
import design
import auxiliare
import globalvariable
import functie1
import functie2
import functie3
import functie4
import functie5
import functie6

def test_functie_verificare_numar_natural():

    assert auxiliare.functie_verificare_numar_natural('10') == 10
    assert auxiliare.functie_verificare_numar_natural('0') == 0
    assert auxiliare.functie_verificare_numar_natural('25') == 25
    assert auxiliare.functie_verificare_numar_natural('100') == 100
    assert auxiliare.functie_verificare_numar_natural('2001') == 2001

def test_functie_verificare_numar():

    assert auxiliare.functie_verificare_numar('-1') == -1
    assert auxiliare.functie_verificare_numar('-100') == -100
    assert auxiliare.functie_verificare_numar('-20') == -20
    assert auxiliare.functie_verificare_numar('-10') == -10
    assert auxiliare.functie_verificare_numar('-2001') == -2001

def test_functie_1_1():

    assert functie1.functie_1_1([[1,2],[3,4],[1,2],[4,2],[5,6],[7,8],[8,6],[6,8]],6+2j) == [[1,2],[3,4],[1,2],[4,2],[5,6],[7,8],[8,6],[6,8],[6,2]]
    #assert functie1.functie_1_1([[1,2],[3,4],[1,2],[4,2],[5,6],[7,8],[8,6],[6,8]],-1+2j) == [1+2j,3+4j,1+2j,4+2j,5+6j,7+8j,8+6j,6+8j,-1+2j]
    #assert functie1.functie_1_1([[1,2],[3,4],[1,2],[4,2],[5,6],[7,8],[8,6],[6,8]],-2-2j) == [1+2j,3+4j,1+2j,4+2j,5+6j,7+8j,8+6j,6+8j,-2-2j]
    #assert functie1.functie_1_1([[1,2],[3,4],[1,2],[4,2],[5,6],[7,8],[8,6],[6,8]],10-5j) == [1+2j,3+4j,1+2j,4+2j,5+6j,7+8j,8+6j,6+8j,10-5j]
    #assert functie1.functie_1_1([[1,2],[3,4],[1,2],[4,2],[5,6],[7,8],[8,6],[6,8]],8+9j) == [1+2j,3+4j,1+2j,4+2j,5+6j,7+8j,8+6j,6+8j,8+9j]

def test_functie_1_2():
    
    assert functie1.functie_1_2([[1,2],[3,4],[1,2],[4,2],[5,6],[7,8],[8,6],[6,8]],6+2j,0) == [[6,2],[1,2],[3,4],[1,2],[4,2],[5,6],[7,8],[8,6],[6,8]]
    #assert functie1.functie_1_2([1+2j,3+4j,1+2j,4+2j,5+6j,7+8j,8+6j,6+8j],-1+2j,3) == [1+2j,3+4j,1+2j,-1+2j,4+2j,5+6j,7+8j,8+6j,6+8j]
    #assert functie1.functie_1_2([1+2j,3+4j,1+2j,4+2j,5+6j,7+8j,8+6j,6+8j],-2-2j,8) == [1+2j,3+4j,1+2j,4+2j,5+6j,7+8j,8+6j,6+8j,-2-2j]
    #assert functie1.functie_1_2([1+2j,3+4j,1+2j,4+2j,5+6j,7+8j,8+6j,6+8j],10-5j,5) == [1+2j,3+4j,1+2j,4+2j,5+6j,10-5j,7+8j,8+6j,6+8j]
    #assert functie1.functie_1_2([1+2j,3+4j,1+2j,4+2j,5+6j,7+8j,8+6j,6+8j],8+9j,1) == [1+2j,8+9j,3+4j,1+2j,4+2j,5+6j,7+8j,8+6j,6+8j]

def test_functie_2_1():

    assert functie2.functie_2_1([[1,2],[3,4],[1,2],[4,2],[5,6],[7,8],[8,6],[6,8]],0) == [[3,4],[1,2],[4,2],[5,6],[7,8],[8,6],[6,8]]
    #assert functie2.functie_2_1([1+2j,3+4j,1+2j,4+2j,5+6j,7+8j,8+6j,6+8j],7) == [1+2j,3+4j,1+2j,4+2j,5+6j,7+8j,8+6j]
    #assert functie2.functie_2_1([1+2j,3+4j,1+2j,4+2j,5+6j,7+8j,8+6j,6+8j],1) == [1+2j,1+2j,4+2j,5+6j,7+8j,8+6j,6+8j]
    #assert functie2.functie_2_1([1+2j,3+4j,1+2j,4+2j,5+6j,7+8j,8+6j,6+8j],3) == [1+2j,3+4j,1+2j,5+6j,7+8j,8+6j,6+8j]
    #assert functie2.functie_2_1([1+2j,3+4j,1+2j,4+2j,5+6j,7+8j,8+6j,6+8j],5) == [1+2j,3+4j,1+2j,4+2j,5+6j,8+6j,6+8j]

def test_functie_2_2():
    
    assert functie2.functie_2_2([[1,2],[3,4],[1,2],[4,2],[5,6],[7,8],[8,6],[6,8]],0,1) == [[1,2],[4,2],[5,6],[7,8],[8,6],[6,8]]
    #assert functie2.functie_2_2([1+2j,3+4j,1+2j,4+2j,5+6j,7+8j,8+6j,6+8j],7,7) == [1+2j,3+4j,1+2j,4+2j,5+6j,7+8j,8+6j]
    #assert functie2.functie_2_2([1+2j,3+4j,1+2j,4+2j,5+6j,7+8j,8+6j,6+8j],1,3) == [1+2j,5+6j,7+8j,8+6j,6+8j]
    #assert functie2.functie_2_2([1+2j,3+4j,1+2j,4+2j,5+6j,7+8j,8+6j,6+8j],3,5) == [1+2j,3+4j,1+2j,8+6j,6+8j]
    #assert functie2.functie_2_2([1+2j,3+4j,1+2j,4+2j,5+6j,7+8j,8+6j,6+8j],7,5) == [1+2j,3+4j,1+2j,4+2j,5+6j]

def test_functie_2_3():
    
    assert functie2.functie_2_3([[1,2],[3,4],[1,2],[4,2],[5,6],[7,8],[8,6],[6,8]],1+2j,9+9j) == [[9,9],[3,4],[9,9],[4,2],[5,6],[7,8],[8,6],[6,8]]
    #assert functie2.functie_2_3([1+2j,3+4j,1+2j,4+2j,5+6j,7+8j,8+6j,6+8j],3+4j,-1-1j) == [1+2j,-1-1j,1+2j,4+2j,5+6j,7+8j,8+6j,6+8j]
    #assert functie2.functie_2_3([1+2j,3+4j,1+2j,4+2j,5+6j,7+8j,8+6j,8+6j],8+6j,20+20j) == [1+2j,3+4j,1+2j,4+2j,5+6j,7+8j,20+20j,20+20j]
    #assert functie2.functie_2_3([1+2j,1+2j,1+2j,1+2j,1+2j,1+2j,1+2j,1+2j],1+2j,10+20j) == [10+20j,10+20j,10+20j,10+20j,10+20j,10+20j,10+20j,10+20j]
    #assert functie2.functie_2_3([1+2j,3+4j,1+2j,4+2j,5+6j,7+8j,8+6j,6+8j],9+9j,10-11j) == [1+2j,3+4j,1+2j,4+2j,5+6j,7+8j,8+6j,6+8j]

def test_functie_sortare():

    assert functie4.sortare([[1,1],[2,2],[3,3],[4,4],[5,5]]) == [[5,5],[4,4],[3,3],[2,2],[1,1]]
    #assert functie4.sortare([1+5j,2+4j,3+3j,4+2j,5+1j]) == [1+5j,2+4j,3+3j,4+2j,5+1j]
    #assert functie4.sortare([1+5j,2+4j,3+3j,4+2j,5+6j]) == [5+6j,1+5j,2+4j,3+3j,4+2j]
    #assert functie4.sortare([2+3j,3+1j,4+5j,3+3j,3+2j]) == [4+5j,2+3j,3+3j,3+2j,3+1j]
    #assert functie4.sortare([3+1j,4+5j,2+3j,10+4j,20+2j]) == [4+5j,10+4j,2+3j,20+2j,3+1j]

def test_functie_4_1():
    
    assert functie4.functie_4_1([[1,1],[2,2],[3,3]],0,2) == 6+6j
    #assert functie4.functie_4_1([1+1j,2+2j,3+3j,3-3j],2,3) == 6+0j 
    #assert functie4.functie_4_1([1+1j,2+2j,3+3j,-3-3j],1,2) == 5+5j 
    #assert functie4.functie_4_1([1+1j,2+2j,3+3j,-6-6j],0,3) == 0+0j
    #assert functie4.functie_4_1([1+1j,2+2j,3+3j,4+4j],0,3) == 10+10j  

def test_functie_4_2():
        
    assert functie4.functie_4_2([[1,1],[2,2],[3,3]],0,0) == 1+1j
    #assert functie4.functie_4_2([1+1j,2+2j,3+3j,0-0j],0,3) == 0+0j
    #assert functie4.functie_4_2([1+1j,2+2j,3+3j,-3-3j],0,2) == -12+12j 
    #assert functie4.functie_4_2([1+1j,2+2j,3+3j,-6-6j],2,3) == 0-36j
    #assert functie4.functie_4_2([1+1j,3+2j,3+3j,4+4j],0,1) == 1+5j

def test_functie_4_3():

    assert functie4.functie_4_3([[1,1],[2,2]]) == [[2,2],[1,1]]
    #assert functie4.functie_4_3([1+1j,2+2j,3+3j]) == [3+3j,2+2j,1+1j]
    #assert functie4.functie_4_3([1+1j,2+2j,3+3j,4+4j]) == [4+4j,3+3j,2+2j,1+1j]
    #assert functie4.functie_4_3([2+3j,3+1j,4+5j,3+3j,3+2j]) == [4+5j,2+3j,3+3j,3+2j,3+1j]
    #assert functie4.functie_4_3([3+1j,4+5j,2+3j,10+4j,20+2j]) == [4+5j,10+4j,2+3j,20+2j,3+1j]

def test_prim():
    
    assert functie5.prim(5) == 1
    assert functie5.prim(-5) == 0
    assert functie5.prim(25) == 0
    assert functie5.prim(7) == 1
    assert functie5.prim(11) == 1

def test_functie_5_1():

    assert functie5.functie_5_1([[1,2],[1,3],[2,2]]) == [[1,2],[1,3]]
    #assert functie5.functie_5_1([1+2j,1+3j,2+2j,5+5j]) == [1+2j,1+3j]
    #assert functie5.functie_5_1([1+2j,1+3j,2+2j,7-9j]) == [1+2j,1+3j]
    #assert functie5.functie_5_1([1+2j,1+3j,2+2j,4+3j]) == [1+2j,1+3j,4+3j]
    #assert functie5.functie_5_1([2+2j,2+3j,2+2j]) == []

def test_functie_5_2_1():

    assert functie5.functie_5_2_1([[1,1],[2,2]],2) == [[2,2]] 
    #assert functie5.functie_5_2_1([1+1j,2+2j],3) == []
    #assert functie5.functie_5_2_1([1+1j,2+2j],1) == [1+1j,2+2j] 
    #assert functie5.functie_5_2_1([1+1j,2+2j,3+3j,4+4j],4) == [3+3j,4+4j]
    #assert functie5.functie_5_2_1([5+1j,3+4j],0) == [5+1j,3+4j]

def test_functie_5_2_2():

    assert functie5.functie_5_2_2([[2,0],[2,2]],2) == [[2,2]] 
    #assert functie5.functie_5_2_2([1+1j,2+2j],3) == [1+1j,2+2j]
    #assert functie5.functie_5_2_2([1+0j,0+1j],1) == [] 
    #assert functie5.functie_5_2_2([1+1j,2+2j,3+3j,4+0j],4) == [1+1j,2+2j,3+3j]
    #assert functie5.functie_5_2_2([5+1j,3+4j],0) == [5+1j,3+4j]

def test_functie_5_2_3():
    
    assert functie5.functie_5_2_3([[2,0],[2,2]],2) == [[2,0]] 
    #assert functie5.functie_5_2_3([1+1j,2+2j],3) == [1+1j,2+2j]
    #assert functie5.functie_5_2_3([1+0j,0+1j],0) == [] 
    #assert functie5.functie_5_2_3([1+1j,2+2j,3+3j,4+0j],2) == [1+1j]
    #assert functie5.functie_5_2_3([5+1j,3+4j],5) == [3+4j]

def rulare_teste():

    test_functie_1_1()
    test_functie_1_2()
    test_functie_2_1()
    test_functie_2_2()
    test_functie_2_3()
    test_functie_4_1()
    test_functie_4_2()
    test_functie_4_3()
    test_functie_5_1()
    test_functie_5_2_1()
    test_functie_5_2_2()
    test_functie_5_2_3()
    test_functie_sortare()
    test_functie_verificare_numar()
    test_functie_verificare_numar_natural()
    test_prim()
    globalvariable.copie = []
    globalvariable.contor = 0

