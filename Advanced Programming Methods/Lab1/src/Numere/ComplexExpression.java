package Numere;

/**
 *      ComplexExpression este o clasa abstracta, din care mostenesc cele 4 clase ce se ocupa cu operatiile pe numere complexe
 */
public abstract class ComplexExpression {

    private Operation operation;
    private ComplexNumber[] args;

    /**
     * Aceasta este constructorul clasei ComplexExpression, ce primeste ca si parametrii:
     * @param op - Operation - retinem operatia pe care o sa o efectueze clasa
     * @param vec - NumarComplex[] - retinem vectorul de numere complexe
     */
    public ComplexExpression(Operation op, ComplexNumber[] vec){

        this.operation = op;
        this.args = vec;
    }

    /**
     *
     * @param nr1
     * @param nr2
     * @return Un numar complex acesta fiind rezultatul operatiei, dar metoda nu este implementata pentru ca este abstracta si urmeaza a fi implementata de clasele ce o sa
     *         mosteneasca clasa ComplexExpression
     */
    protected abstract ComplexNumber executeOneOperation(ComplexNumber nr1, ComplexNumber nr2);

    /**
     * Metoda execute se ocupa cu calcularea expresiei
     * @return Rezultatul unei expresii
     */
    public ComplexNumber execute(){

        ComplexNumber rez = args[0];

        for(int i = 1; i < args.length; i++){

            rez = executeOneOperation(rez, args[i]);
        }

        return rez;
    }

    /**
     *  Suprascriem metoda toString pentru a afisa numerele complex in formatul dorit de noi
     */
    @Override
    public String toString(){

        String semn;

        String rezultat = "";

        semn = this.operation.getSymbol();

        for(int i = 0; i < args.length; i++){

            rezultat = rezultat + args[i].toString() + " ";

            if(i == args.length - 1)

                rezultat += "= ";

            else

                rezultat += semn + " ";
        }

        return rezultat;
    }
}
