package Operatii;

import Numere.ComplexExpression;
import Numere.ComplexNumber;
import Numere.Operation;

/**
 *  Aceasta clasa se ocupa cu efectuarea operatiei de impartire si mosteneste din calsa ComplexExpression si totodata suprascrie metoda abstracta mostenita
 */
public class ExecuteDivision extends ComplexExpression {

    /**
     * Constructorul clasei noastre ce il apeleaza pe cel al clasei mostenite
     * @param op - Operation - operatia corespunzatoare impartirii
     * @param vec - NumarComplex[] - vectorul de numere complexe
     */
    public ExecuteDivision(Operation op, ComplexNumber[] vec){

        super(op, vec);
    }

    /**
     * Aceasta este metoda mostenita ce trebuie suprscrisa ea fiind declarata abstracta in clasa de unde mosteneste si se ocupa cu realizarea impartirii a 2 numere complexe
     * @param nr1 - NumarComplex - Primul numar complex - deimpartitul
     * @param nr2 - NumarComplex - Al doilea numar complex - impartitorul
     * @return rez - NumarComplex - Rezultatul impartirii
     */
    @Override
    public ComplexNumber executeOneOperation(ComplexNumber nr1, ComplexNumber nr2) {

        ComplexNumber rez = nr1.impartire(nr2);
        return rez;
    }
}
