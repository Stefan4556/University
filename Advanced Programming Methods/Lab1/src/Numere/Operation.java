package Numere;

/**
 * Acest enum retine operatiile ce pot aparea in cadrul expresiilor noastre
 */
public enum Operation{

    ADDITION("+"),    SUBSTRACTION("-"),    MULTIPLICATION("*"),    DIVISION("/");

    private String symbol;

    /**
     * Acesta este constructorul enum-ului nostru
     * @param symbol - String - simbolul corespunzator operatiei noastre
     */
    Operation(String symbol){

        this.symbol = symbol;
    }

    /**
     * Metoda ce se ocupa cu returnarea unei operatii corespunzatoare unui simbol
     * @param symbol - String - Semnul corespunzator operatiei noastre
     * @return Operation - Operatia cautata
     */
    public static Operation getBySymbol(String symbol){

        for(Operation op : Operation.values())

            if(op.symbol.equals(symbol))

                return op;

        return null;
    }

    /**
     * Acesta este getter-ul pentru simbol
     * @return symbol - String
     */
    public String getSymbol(){

        return symbol;
    }
};