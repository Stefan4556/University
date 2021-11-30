package Parser;

import Numere.ComplexExpression;
import Numere.ComplexNumber;
import Numere.Operation;
import Singleton.ExpressionFactory;

import java.util.Objects;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class ExpressionParser {

    public ComplexExpression parseExpression(String[] args){

        isValid(args);

        ComplexNumber[] vec = buildArgs(args);

        Operation op = Operation.getBySymbol(args[1]);

        ExpressionFactory exp = ExpressionFactory.getInstance();

        return exp.createExpression(op, vec);

    }

    private ComplexNumber[] buildArgs(String[] args){

        ComplexNumber[] vector = new ComplexNumber[args.length / 2 + 1];
        int poz = 0;

        String Pattern1 = "-?(\\d+)[+-]-?(\\d*)\\*?i";
        String Pattern11 = "-?(\\d+)[+-]-(\\d*)\\*?i";  // cazul cand avem la a + -b * i
        String Pattern12 ="-?(\\d+)-(\\d*)\\*?i";       // cazul cand avem a - b * i
        String Pattern13 = "-(\\d+)[+-]-?(\\d*)\\*?i";
        String Pattern2 = "-?(\\d+)";
        String Pattern3 = "-?(\\d*)\\*?i";
        String Pattern31 = "-(\\d*)\\*?i";

        // Distingem 3 cazuri:
        //      1) Cand corespunde numerelor de forma pattern1
        //      2) Cand corespunde numerelor de forma pattern2
        //      3) Cand corespunde numerelor de forma pattern3
        for(int i = 0; i < args.length; i += 2){

            if(args[i].matches(Pattern1)){

                Pattern r = Pattern.compile(Pattern1);
                Matcher m = r.matcher(args[i]);
                if(m.find()) {

                    double real = Integer.parseInt(m.group(1));
                    double imag;
                    if(!Objects.equals(m.group(2), ""))

                        imag = Integer.parseInt(m.group(2));

                    else

                        imag = 1;

                    if (args[i].matches(Pattern13))

                        real *= -1;

                    if (args[i].matches(Pattern11) || args[i].matches(Pattern12))

                        imag *= -1;

                    ComplexNumber nr = new ComplexNumber(real, imag);
                    vector[poz] = nr;
                    poz++;
                }
            }
            else if(args[i].matches(Pattern2)){ // parte reala

                double real = Integer.parseInt(args[i]);
                double imag = 0;

                ComplexNumber nr = new ComplexNumber(real, imag);
                vector[poz] = nr;
                poz++;
            }
            else{   // parte imaginara

                double real = 0;

                Pattern r = Pattern.compile(Pattern3);
                Matcher m = r.matcher(args[i]);
                if(m.find()) {

                    double imag;

                    if(!Objects.equals(m.group(1), ""))

                        imag = Integer.parseInt(m.group(1));

                    else

                        imag = 1;

                    if (args[i].matches(Pattern31))

                        imag *= -1;

                    ComplexNumber nr = new ComplexNumber(real, imag);
                    vector[poz] = nr;
                    poz++;
                }
            }
        }

        return vector;
    }

    private void isValid(String[] args){

        // Testam daca numarul de argumente este impar
        try {

            if (args.length % 2 == 0)

                throw new ExceptieParser("Numarul de argumente este par!");

        } catch(ExceptieParser er){

            System.err.println(er.getMessage());
            System.exit(1);
        }

        // Testam ca numarul de semne este cu 1 mai putin decat numarul de numere
        int nr_semne = 0;
        try{

            int nr_numere = 0;

            for(String el : args){

                if(Objects.equals(el, "-") || Objects.equals(el, "+") || Objects.equals(el, "*") || Objects.equals(el, "/"))

                    nr_semne++;

                else

                    nr_numere++;
            }

            if(nr_numere - 1 != nr_semne || nr_semne == 0)

                throw new ExceptieParser("Numarul de semne nu este egal cu numarul de numere - 1!");
        } catch(ExceptieParser er){

            System.err.println(er.getMessage());
            System.exit(1);
        }

        //Verificam daca semnele sunt pe pozitii impare
        try{

            int nr_semn_poz_imp = 0;

            for(int i = 1; i < args.length; i+=2)

                if(Objects.equals(args[i], "+") || Objects.equals(args[i], "-") || Objects.equals(args[i], "*") || Objects.equals(args[i], "/"))

                    nr_semn_poz_imp++;

            if(nr_semn_poz_imp != nr_semne)

                throw new ExceptieParser("Semnele nu se gasesc pe pozitii impare!");

        } catch(ExceptieParser er){

            System.err.println(er.getMessage());
            System.exit(1);
        }

        // Testam daca semnele sunt egale
        try{

            String semn = args[1];

            for(int i = 3; i < args.length; i+= 2)

                if(!Objects.equals(args[i], semn))

                    throw new ExceptieParser("Semnele nu sunt egale!");

        } catch(ExceptieParser er){

            System.err.println(er.getMessage());
            System.exit(1);
        }

        // Trebuie sa validam si numerele sa fie complexe si sa se incadreze in unul din patternuri
        // parte reala si imaginara -- -?(\d+)[+-]-?(\d+)\*?i
        // parte reala              -- -?(\d+)
        // parte imaginara          -- -?(\d+)\*?i
        try{

            String Pattern1 = "-?(\\d+)[+-]-?(\\d*)\\*?i";
            String Pattern2 = "-?(\\d+)";
            String Pattern3 = "-?(\\d*)\\*?i";

            for(int i = 0 ; i < args.length; i+= 2)

                if(!args[i].matches(Pattern1) && !args[i].matches(Pattern2) && !args[i].matches(Pattern3))

                    throw new ExceptieParser("Numarul " + args[i] + " nu este valid!");

        } catch(ExceptieParser er){

            System.err.println(er.getMessage());
            System.exit(1);
        }
    }
}
