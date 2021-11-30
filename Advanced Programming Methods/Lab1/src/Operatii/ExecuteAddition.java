package Operatii;

import Numere.ComplexExpression;
import Numere.ComplexNumber;
import Numere.Operation;

/**
 *  Aceasta clasa se ocupa cu efectuarea operatiei de adaugare si mosteneste din calsa ComplexExpression si totodata suprascrie metoda abstracta mostenita
 */
public class ExecuteAddition extends ComplexExpression {

    /**
     * Constructorul clasei noastre ce il apeleaza pe cel al clasei mostenite
     * @param op - Operation - operatia corespunzatoare adunarii
     * @param vec - NumarComplex[] - vectorul de numere complexe
     */
    public ExecuteAddition(Operation op, ComplexNumber[] vec){

        super(op,vec);
    }

    /**
     * Aceasta este metoda mostenita ce trebuie suprscrisa ea fiind declarata abstracta in clasa de unde mosteneste si se ocupa cu realizarea adunarii a 2 numere complexe
     * @param nr1 - NumarComplex - Primul numar complex pe care-l adaugam
     * @param nr2 - NumarComplex - Al doilea numar complex pe care-l adaugam
     * @return rez - NumarComplex - Rezultatul adunarii
     */
    @Override
    public ComplexNumber executeOneOperation(ComplexNumber nr1, ComplexNumber nr2) {

        ComplexNumber rez = nr1.adunare(nr2);
        return rez;
    }
}
