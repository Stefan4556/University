package Numere;

/**
 *  Clasa NumarComplex se ocupa cu retinerea a 2 campuri si metodele aferente acesteia
 */
public class ComplexNumber {

    private double re;
    private double im;

    /**
     * Constructorul clasei NumarComplex ce primeste ca si parametru:
     * @param re - double - Partea reala a numarului complex
     * @param im - double - Partea imaginara a numarului complex
     */
    public ComplexNumber(double re, double im){

        this.re = re;
        this.im = im;
    }

    /**
     * Getter-ul pentru partea reala a unui numar complex
     * @return double - partea reala a numarului complex
     */
    public double getRe() {
        return re;
    }

    /**
     * Getter-ul pentru partea imaginara a unui numar complex
     * @return double - partea imaginara a numarului complex
     */
    public double getIm() {
        return im;
    }

    /**
     * Metoda se ocupa cu adunarea a 2 numere complexe, unul dintre ele fiind primit ca si parametru
     * @param n - NumarComplex, numarul pe care-l adunam la numarul nostru
     * @return rez - NumarComplex, rezultatul adunarii celor 2 numere complexe
     */
    public ComplexNumber adunare(ComplexNumber n){

        this.re = this.re + n.re;
        this.im = this.im + n.im;

        return new ComplexNumber(this.re, this.im);
    }

    /**
     * Metoda se ocupa cu scaderea a 2 numere complexe, unul dintre ele fiind primit ca si parametru
     * @param n - NumarComplex, numarul pe care-l scadem din numarul nostru
     * @return rez - NumarComplex, rezultatul scaderii celor 2 numere complexe
     */
    public ComplexNumber scadere(ComplexNumber n){

        this.re = this.re - n.re;
        this.im = this.im - n.im;

        return new ComplexNumber(this.re, this.im);
    }

    /**
     * Metoda se ocupa cu inmultirea a 2 numere complexe, unul dintre ele fiind primit ca si parametru
     * @param n - NumarComplex, numarul pe care-l adunam la numarul nostru
     * @return rez - NumarComplex, rezultatul inmultirii celor 2 numere complexe
     */
    public ComplexNumber inmultire(ComplexNumber n){

        double real = this.re * n.re - this.im * n.im;
        double imaginar = this.re * n.im + this.im * n.re;

        return new ComplexNumber(real, imaginar);
    }

    /**
     * Aceasta metoda se ocupa cu aflarea conjugatului numarului nostru complex
     */
    public void conjugatul(){

        this.im = -1 * this.im;
    }

    /**
     * Metoda se ocupa cu impartirea a 2 numere complexe, unul dintre ele fiind primit ca si parametru
     * @param n - NumarComplex, reprezentand impartitorul
     * @return rez - NumarComplex, rezultatul adunarii celor 2 numere complexe
     */
    public ComplexNumber impartire(ComplexNumber n){

        n.conjugatul();
        ComplexNumber rez_i = this.inmultire(n);

        double numitor = n.re * n.re + n.im * n.im;

        this.re = rez_i.re / numitor;
        this.im = rez_i.im / numitor;

        return new ComplexNumber(this.re, this.im);
    }

    /**
     * Suprascriem metoda string pentru a putea afisa un numar complex
     * @return String - returneaza forma dorita a numarului complex
     */
    @Override
    public String toString(){

        String real_s = String.valueOf(this.re);
        String imag_s = String.valueOf(this.im);
        return real_s + " + " + imag_s + " * i";
    }
}
