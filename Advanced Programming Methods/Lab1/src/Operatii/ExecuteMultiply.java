package Operatii;

import Numere.ComplexExpression;
import Numere.ComplexNumber;
import Numere.Operation;

/**
 *  Aceasta clasa se ocupa cu efectuarea operatiei de inmultire si mosteneste din calsa ComplexExpression si totodata suprascrie metoda abstracta mostenita
 */
public class ExecuteMultiply extends ComplexExpression {

    /**
     * Constructorul clasei noastre ce il apeleaza pe cel al clasei mostenite
     * @param op - Operation - operatia corespunzatoare inmultirii
     * @param vec - NumarComplex[] - vectorul de numere complexe
     */
    public ExecuteMultiply(Operation op, ComplexNumber[] vec){

        super(op, vec);
    }

    /**
     * Aceasta este metoda mostenita ce trebuie suprscrisa ea fiind declarata abstracta in clasa de unde mosteneste si se ocupa cu realizarea inmultirii a 2 numere complexe
     * @param nr1 - NumarComplex - Primul numar complex pe care-l inmultim
     * @param nr2 - NumarComplex - Al doilea numar complex pe care-l inmultim
     * @return rez - NumarComplex - Rezultatul inmultirii
     */
    @Override
    public ComplexNumber executeOneOperation(ComplexNumber nr1, ComplexNumber nr2) {

        ComplexNumber rez = nr1.inmultire(nr2);
        return rez;
    }
}
