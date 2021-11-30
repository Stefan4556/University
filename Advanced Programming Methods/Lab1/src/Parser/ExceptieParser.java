package Parser;

/**
 *  Clasa ExceptieParser se ocupa cu prinderea exceptiilor ce pot aparea la nivelul parser-ului
 */
public class ExceptieParser extends Exception{

    /**
     * Acesta este constructorul clasei, ce apeleaza constructorul lui Exception, dat fiind faptul ca mosteneste din aceasta clasa
     * @param message - Mesajul ce consta in eroarea noastra
     */
    public ExceptieParser(String message){

        super(message);
    }
}
