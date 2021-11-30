package Singleton;

import Numere.ComplexExpression;
import Numere.ComplexNumber;
import Numere.Operation;
import Operatii.ExecuteAddition;
import Operatii.ExecuteMultiply;
import Operatii.ExecuteSubstraction;
import Operatii.ExecuteDivision;

/**
 * Aceasta este clasa ce se ocupa cu realizarea sablonului de proiectare singleton
 */
public class ExpressionFactory {

    /**
     * Facem un obiect cu ajutorul acestei metode
     */
    private static ExpressionFactory instance = new ExpressionFactory();

    /**
     * Facem constructorul privat pentru a ne asigura ca aceasta clasa nu poate fi initializata
     */
    private ExpressionFactory(){}

    /**
     * Aceasta metoda returneaza singurul obiect facut
     * @return instance - ExpressionFactory - unicul obiect facut
     */
    public static ExpressionFactory getInstance(){

        return instance;
    }

    /**
     * Cu ajutorul acestei metode realizam expresia noastra, pe care o pregatim de calculare
     * @param op - Operation - operatia noastra
     * @param vec - NumarComplex[] - lista de numere complexe
     * @return rez - ComplexExpression - returneaza tipul relatiei
     */
    public ComplexExpression createExpression(Operation op, ComplexNumber[] vec){

        if(op == Operation.ADDITION) {

            ExecuteAddition rez = new ExecuteAddition(op, vec);
            return rez;
        }
        else if(op == Operation.SUBSTRACTION){
            ExecuteSubstraction rez = new ExecuteSubstraction(op, vec);
            return rez;
        }
        else if(op == Operation.MULTIPLICATION){
            ExecuteMultiply rez = new ExecuteMultiply(op, vec);
            return rez;
        }
        else{
            ExecuteDivision rez = new ExecuteDivision(op, vec);
            return rez;
        }
        /*
        ComplexExpression rez = null;

        switch(op){
            case ADDITION: rez =  new ExecuteAddition(op, vec);
            case SUBSTRACTION: rez =  new ExecuteSubstraction(op, vec);
            case MULTIPLICATION: rez = new ExecuteMultiply(op, vec);
            case DIVISION: rez =  new ExecuteDivision(op, vec);
        };*/
    }
}
