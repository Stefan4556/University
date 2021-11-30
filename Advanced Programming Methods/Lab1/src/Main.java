import Numere.ComplexExpression;
import Numere.ComplexNumber;
import Parser.ExpressionParser;
import Teste.Teste;

/**
 * Clasa Main este clasa ce se ocupa cu pornirea programului si apelarea metodelor aferente pentru a citi, afisa si calcula corect o expresie formata din numere complexe
 */
public class Main {

    /**
     * Aceasta este metoda ce face toate apelurile necesare pentru ca a porni programul nostru
     * @param args - String[] - argumentele primite din linia de comanda
     */
    public static void main(String[] args) {

        Teste t = new Teste();
        t.ruleazaTeste();

        System.out.println("Salut!");

        ExpressionParser par = new ExpressionParser();

        ComplexExpression run = par.parseExpression(args);

        System.out.print(run.toString());

        ComplexNumber rez = run.execute();

        System.out.println(rez.toString());
    }
}

// 2-3*i + 2+3*i + 2+3*i + -2i + -2 + -2 + 2i = 2 + 3i
// t1 : 2+3*i + 2+3*i + 2+3*i = 6 + 9 * i
// t2 : 2+3*i - 2+3*i - 2+3*i = -2 + -3 * i
// t3 : 1+3*i * 2+2*i = -4 + 8 * i
// t4 : 1+3*i / 2-2*i = -0,5 + i
// t5 : -2+2i + 3 + -1*i + 1+i + i + -i + 1 + -1 = 2 + 2i
// t6 : 2-3*i + 2+3*i + 2+3*i + -2i + -2 + -2 + 2i = 2 + 3i
// Teste ce arunca exceptii
// t1 : 2 2 - numarul de elemente este par
// t2 : 2 2 2 - nr de semne nu e egal cu nr de numere - 1
// t3 : 2 2 - - semnele nu se gasesc pe pozitii impare
// t4 : 2 - 2 + 2 - semnele nu sunt egale
// t5 : a + 2 - numarul a nu e valid
