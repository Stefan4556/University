package Teste;

import Numere.ComplexExpression;
import Numere.ComplexNumber;
import Parser.ExpressionParser;

import java.util.Objects;

/**
 * Aceasta este clasa ce contine mai multe metode ce se ocupa cu testarea tuturor claselor facute
 */
public class Teste {

    /**
     * Dupa cum ii si spune numele, aceasta functie se ocupa cu testarea metodei de adunare a numerelor complexe
     */
    private void testAdunare(){

        ComplexNumber n1 = new ComplexNumber(2,2);
        ComplexNumber n2 = new ComplexNumber(2,2);
        ComplexNumber rez = n1.adunare(n2);
        assert rez.getRe() == 4;
        assert rez.getIm() == 4;

        n1 = new ComplexNumber(2, -2);
        n2 = new ComplexNumber(-2,2);
        rez = n1.adunare(n2);
        assert rez.getRe() == 0;
        assert rez.getIm() == 0;

        System.out.println("Testele la adunare au rulat cu succes!");
    }

    /**
     * Dupa cum ii si spune numele, aceasta functie se ocupa cu testarea metodei de scadere a numerelor complexe
     */
    private void testScadere(){

        ComplexNumber n1 = new ComplexNumber(2,2);
        ComplexNumber n2 = new ComplexNumber(2,2);
        ComplexNumber rez = n1.scadere(n2);
        assert rez.getRe() == 0;
        assert rez.getIm() == 0;

        n1 = new ComplexNumber(-2, 2);
        n2 = new ComplexNumber(-2,-2);
        rez = n1.scadere(n2);
        assert rez.getRe() == 0;
        assert rez.getIm() == 4;

        System.out.println("Testele la scadere au rulat cu succes!");
    }

    /**
     * Dupa cum ii si spune numele, aceasta functie se ocupa cu testarea metodei de inmultire a numerelor complexe
     */
    private void testInmultire(){

        ComplexNumber n1 = new ComplexNumber(2,3);
        ComplexNumber n2 = new ComplexNumber(5,-1);
        ComplexNumber rez = n1.inmultire(n2);
        assert rez.getRe() == 13;
        assert rez.getIm() == 13;

        n1 = new ComplexNumber(-2,-2);
        n2 = new ComplexNumber(-3,-3);
        rez = n1.inmultire(n2);
        assert rez.getRe() == 0;
        assert rez.getIm() == 12;

        n1 = new ComplexNumber(3,3);
        n2 = new ComplexNumber(2,0);
        rez = n1.inmultire(n2);
        assert rez.getRe() == 6;
        assert rez.getIm() == 6;

        System.out.println("Testele  la inmultire au rulat cu succes!");
    }

    /**
     * Dupa cum ii si spune numele, aceasta functie se ocupa cu testarea metodei de impartire a numerelor complexe
     */
    private void testImpartire(){

        ComplexNumber n1 = new ComplexNumber(6,6);
        ComplexNumber n2 = new ComplexNumber(2,2);
        ComplexNumber rez = n1.impartire(n2);
        assert rez.getRe() == 3;
        assert rez.getIm() == 0;

        n1 = new ComplexNumber(6,6);
        n2 = new ComplexNumber(3,0);
        rez = n1.impartire(n2);
        assert rez.getRe() == 2;
        assert rez.getIm() == 2;

        System.out.println("Testele la imparitre au rulat cu succes!");
    }

    /**
     * Dupa cum ii si spune numele, aceasta functie se ocupa cu testarea metodei ce se ocupa cu validarea datelor
     */
    private void testValidator(){

        ExpressionParser p = new ExpressionParser();

        String[] args1 = new String[3];
        args1[0] = "2+3i";
        args1[1] = "+";
        args1[2] = "i";
        p.parseExpression(args1);

        String[] args2 = new String[3];
        args2[0] = "2+3i";
        args2[1] = "-";
        args2[2] = "i";
        p.parseExpression(args2);

        String[] args3 = new String[3];
        args3[0] = "2+3i";
        args3[1] = "*";
        args3[2] = "i";
        p.parseExpression(args3);

        String[] args4 = new String[3];
        args4[0] = "2-3i";
        args4[1] = "/";
        args4[2] = "i";
        p.parseExpression(args4);

        System.out.println("Testele la validator au rulat cu succes!");
    }

    /**
     * Dupa cum ii si spune numele, aceasta functie se ocupa cu testarea metodei de calculare a metodei ce se ocupa cu calcularea unei expresii
     */
    private void testExecute(){

        ExpressionParser p = new ExpressionParser();

        String[] args1 = new String[3];
        args1[0] = "2+3i";
        args1[1] = "+";
        args1[2] = "i";
        ComplexExpression e1 = p.parseExpression(args1);
        ComplexNumber rez1 = e1.execute();
        assert rez1.getRe() == 2;
        assert rez1.getIm() == 4;

        String[] args2 = new String[3];
        args2[0] = "2";
        args2[1] = "-";
        args2[2] = "i";
        ComplexExpression e2 = p.parseExpression(args2);
        ComplexNumber rez2 = e2.execute();
        assert rez2.getRe() == 2;
        assert rez2.getIm() == -1;

        String[] args3 = new String[3];
        args3[0] = "2+-3i";
        args3[1] = "*";
        args3[2] = "i";
        ComplexExpression e3 = p.parseExpression(args3);
        ComplexNumber rez3 = e3.execute();
        assert rez3.getRe() == 3;
        assert rez3.getIm() == 2;

        String[] args4 = new String[3];
        args4[0] = "2-4i";
        args4[1] = "/";
        args4[2] = "2";
        ComplexExpression e4 = p.parseExpression(args4);
        ComplexNumber rez4 = e4.execute();
        assert rez4.getRe() == 1;
        assert rez4.getIm() == -2;

        System.out.println("Testele la execute au rulat cu succes!");
    }

    /**
     * Dupa cum ii si spune numele, aceasta functie se ocupa cu testarea metodei toString, metoda ce returneaza expresia sub forma unui string
     */
    public void testToString(){

        ExpressionParser p = new ExpressionParser();

        String[] args1 = new String[3];
        args1[0] = "2+2*i";
        args1[1] = "-";
        args1[2] = "i";
        ComplexExpression e1 = p.parseExpression(args1);
        String e1_s = e1.toString();

        if(Objects.equals(e1_s, "2.0 + 2.0 * i - 0.0 + 1.0 * i = ") == false)

            assert false;

        String[] args2 = new String[3];
        args2[0] = "2+2*i";
        args2[1] = "*";
        args2[2] = "i";
        ComplexExpression e2 = p.parseExpression(args2);
        String e2_s = e2.toString();

        if(Objects.equals(e2_s, "2.0 + 2.0 * i * 0.0 + 1.0 * i = ") == false)

            assert false;

        String[] args3 = new String[3];
        args3[0] = "2+2*i";
        args3[1] = "/";
        args3[2] = "i";
        ComplexExpression e3 = p.parseExpression(args3);
        String e3_s = e3.toString();

        if(Objects.equals(e3_s, "2.0 + 2.0 * i / 0.0 + 1.0 * i = ") == false)

            assert false;

        System.out.println("Testele la afisare au rulat cu succes!");
    }

    /***
     * Codul a fost supus si la alte teste
     */
    public void testVictor(){

        ExpressionParser ep = new ExpressionParser();
        ComplexExpression exp = ep.parseExpression(new String[]{"-5+2*i", "-", "7-3*i", "-", "-5+10*i", "-", "10-5*i"});
        ComplexNumber cn = exp.execute();

        assert (cn.getRe() == -17);
        assert (cn.getIm() == 0);

        exp = ep.parseExpression(new String[]{"20-3*i", "*", "1+4*i", "*", "-2-1*i"});
        cn = exp.execute();

        assert (cn.getRe() == 13);
        assert (cn.getIm() == -186);

        exp = ep.parseExpression(new String[]{"1+2*i", "*", "2-3*i"});
        cn = exp.execute();

        assert (cn.getRe() == 8);
        assert (cn.getIm() == 1);

        exp = ep.parseExpression(new String[]{"3+2*i", "/", "-6-3*i"});
        cn = exp.execute();

        assert (cn.getRe() + 0.53333 < 0.001);
        assert (cn.getIm() + 0.066666 < 0.001);

        exp = ep.parseExpression(new String[]{"2+3*i", "+", "5-6*i", "+", "-2+i", "+", "3-2*i", "+", "5+7*i"});
        cn = exp.execute();

        assert (cn.getRe() == 13);
        assert (cn.getIm() == 3);

        exp = ep.parseExpression(new String[]{"-2", "-", "-3", "-", "5*i", "-", "-7i"});
        cn = exp.execute();

        assert (cn.getRe() == 1);
        assert (cn.getIm() == 2);

        exp = ep.parseExpression(new String[]{"-2i", "+", "-3*i", "+", "5", "+", "-7"});
        cn = exp.execute();

        assert (cn.getRe() == -2);
        assert (cn.getIm() == -5);

        exp = ep.parseExpression(new String[]{"2+3i", "+", "5-6*i", "+", "-2+i"});
        cn = exp.execute();

        assert (cn.getRe() == 5);
        assert (cn.getIm() == -2);

        exp = ep.parseExpression(new String[]{"2+3*i", "+", "-5+10i", "+", "10-5*i", "+", "10+-5i", "+", "-2+i", "+", "-2-i", "+", "-2+-i", "+", "i", "+", "-i", "+", "5", "+", "-7"});
        cn = exp.execute();

        assert (cn.getRe() == 9);
        assert (cn.getIm() == 2);

        exp = ep.parseExpression(new String[]{"i", "+", "-i", "+", "2i", "+", "-2*i"});
        cn = exp.execute();

        assert (cn.getRe() == 0);
        assert (cn.getIm() == 0);

        exp = ep.parseExpression(new String[]{"5","+","6i"});
        cn = exp.execute();

        assert (cn.getRe() == 5);
        assert (cn.getIm() == 6);

    }

    /**
     * Aceasta este metoda apelata in main ce ruleaza toate testele mentionate anterior
     */
    public void ruleazaTeste(){

        System.out.println("Se ruleaza testele...");
        testAdunare();
        testScadere();
        testInmultire();
        testImpartire();
        testValidator();
        testExecute();
        testToString();
        testVictor();
        System.out.println("Testele au fost rulate cu succes!");
    }
}
